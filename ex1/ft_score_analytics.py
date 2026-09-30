#!/usr/bin/env python3
import sys

def main() -> None:
    scores = []
    for arg in sys.argv[1:]:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(scores) == 0:
        print("No scores provided. Usage:"
              " python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        print("=== Player Score Analytics ===")
        players = len(scores)
        total_score = sum(scores)
        average = total_score / players
        highest = max(scores)
        lowest = min(scores)
        score_range = highest - lowest
        print(f"Scores processed: {scores}")
        print(f"Total players: {players}")
        print(f"Total scores: {total_score}")
        print(f"Average score: {average}")
        print(f"High score: {highest}")
        print(f"Low score: {lowest}")
        print(f"Score range: {score_range}")

if __name__ == "__main__":
    main()