package main

import (
	"encoding/json"
	"errors"
	"flag"
	"fmt"
	"math/rand"
	"strconv"
	"time"

	"github.com/hellodhlyn/sqstask"

	us "github.com/hellodhlyn/undersky"
	"github.com/hellodhlyn/undersky/game"
	"github.com/hellodhlyn/undersky/gamer"
	"github.com/hellodhlyn/undersky/libs/s3"
)

var games = map[string]game.Game{
	"1000": &game.Game1000{},
}

func runMatch(payload *us.SubmissionPayload) (match *us.Match) {
	var playerSub us.Submission
	var compSub us.Submission
	us.DB.Where(&us.Submission{ID: payload.PlayerSubmissionID}).First(&playerSub)
	us.DB.Where(&us.Submission{ID: payload.CompetitorSubmissionID}).First(&compSub)

	g, ok := games[payload.GameID]
	if !ok {
		fmt.Printf("invalid game id: %s\n", payload.GameID)
		return nil
	}

	match = us.NewMatch(payload.GameID, playerSub.UserID, playerSub.ID, compSub.UserID, compSub.ID)
	us.DB.Save(match)

	player, err := makeGamer(playerSub)
	if err != nil {
		fmt.Printf("failed to create player: %v\n", err)
		match.Fail("플레이어가 제출한 코드의 실행에 실패했습니다.")
		return
	}

	competitor, err := makeGamer(compSub)
	if err != nil {
		fmt.Printf("failed to create competitor: %v\n", err)
		match.Fail("상대방이 제출한 코드의 실행에 실패했습니다.")
		return
	}

	match.Init()
	matchCtx := game.MatchContext{
		MatchUUID:  payload.MatchUUID,
		Player:     player,
		Competitor: competitor,
	}
	g.InitMatch(&matchCtx)

	// 게임을 시작합니다.
	match.Start()
	var playerWins int
	var competitorWins int
	for i := 0; i < g.GetRuleset().MaximumRound; i++ {
		g.InitRound()

		fmt.Println("starting round...")
		result, err := g.PlayRound()
		if err != nil {
			fmt.Printf("error on playing round: %v\n", err)
			if err == game.ErrPlayerBreakRule {
				match.Fail("플레이어가 규칙에 맞지 않는 결과를 제출했습니다.")
			} else if err == game.ErrCompetitorBreakRule {
				match.Fail("상대방이 규칙에 맞지 않는 결과를 반환했습니다.")
			} else {
				match.Fail("게임의 실행 중 오류가 발생했습니다.")
			}

			return
		}

		if result.WinnerID == player.ID {
			playerWins++
		} else if result.WinnerID == competitor.ID {
			competitorWins++
		}
	}

	fmt.Printf("[Result] Player %d : %d Competitor\n", playerWins, competitorWins)
	match.Finish(g.GetRuleset().MaximumRound, playerWins, competitorWins)

	return
}

func makeGamer(sub us.Submission) (*gamer.Gamer, error) {
	r := rand.New(rand.NewSource(time.Now().UnixNano()))
	port := 10000 + r.Int()%55535

	g := gamer.NewGamer(sub.UserID)

	var driver gamer.ServerDriver
	switch sub.Runtime {
	case "python3.6":
		s3client, err := s3.NewClient("undersky-ai")
		if err != nil {
			return nil, err
		}

		err = s3client.Download(sub.GetS3Key(), "source/"+strconv.Itoa(port)+".py")
		if err != nil {
			return nil, err
		}

		driver = gamer.NewPython3Driver("source." + strconv.Itoa(port))

	default:
		return nil, errors.New("no such runtime: " + sub.Runtime)
	}

	return g, g.StartConnection(port, driver)
}

func main() {
	msg := flag.String("message", "", "sqs message for debug")
	flag.Parse()
	if *msg != "" {
		var payload us.SubmissionPayload
		json.Unmarshal([]byte(*msg), &payload)
		runMatch(&payload)
		return
	}

	task, _ := sqstask.NewSQSTask(&sqstask.Options{
		QueueName:  "undersky-submission",
		AWSRegion:  "ap-northeast-2",
		WorkerSize: 1,
		Consume: func(message string) error {
			var payload us.SubmissionPayload
			json.Unmarshal([]byte(message), &payload)
			runMatch(&payload)
			return nil
		},
		HandleError: func(err error) {
			fmt.Println(err)
		},
	})

	task.StartConsumer()
}
