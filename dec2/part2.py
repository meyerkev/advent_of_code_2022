"""
See problem.txt for the full problem description

The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won)

Rock -> A
Paper -> B
Scissors -> C

--- Part Two ---
The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12.

Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?

Input line format is:
[A-C] [X-Z]
"""

SCORES = {
    "X": {  # They play rock
        "A": 3,  # Play scissors, so 3
        "B": 1,  # Rock
        "C": 2,  # Paper
    },
    "Y": {  # Draw is 3
        "A": 4,
        "B": 5,
        "C": 6
    },
    "Z": {  # Win is 6
        "A": 8,  # Paper
        "B": 9,  # Scissors
        "C": 7  # Rock
    },
}


def main():
    with open('input.txt') as f:
        total_score = 0
        for line in f:
            their_move, your_move = line.strip().split()
            print(SCORES[your_move][their_move])
            total_score += SCORES[your_move][their_move]

    return total_score


if __name__ == "__main__":
    print(main())
