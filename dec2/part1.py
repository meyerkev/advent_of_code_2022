"""
See problem.txt for the full problem description

The score for a single round is the score for the shape you selected 
(1 for Rock, 2 for Paper, and 3 for Scissors) 
plus the score for the outcome of the round 
(0 if you lost, 3 if the round was a draw, and 6 if you won)

Rock -> A and X
Paper -> B and Y
Scissors -> C and Z

Input line format is:
[A-C] [X-Z]
"""

SCORES = {
    "X" : {
        "A": 4,
        "B": 1,
        "C": 7
    }, 
    "Y": {
        "A": 8,
        "B": 5,
        "C": 2
    },
    "Z": {
        "A": 3,
        "B": 9,
        "C": 6
    },
}

def main():
    with open('input.txt') as f:
        total_score = 0 
        for line in f:
            their_move, your_move = line.strip().split()
            print(their_move, your_move, SCORES[your_move][their_move])
            total_score += SCORES[your_move][their_move]

    return total_score

if __name__ == "__main__":
    print(main())
