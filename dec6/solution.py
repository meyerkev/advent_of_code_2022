from collections import Counter
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('distinct_length', nargs='?', type=int,
                        help='The length of the distinct sequence', default=4)
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    with open("input.txt") as f:
        lines = f.readlines()
    input_line = lines[0].strip()
    del lines

    start = 0
    end = args.distinct_length
    character_counts = Counter(input_line[:end])
    if len(character_counts) == args.distinct_length:
        return end

    while end < len(input_line):
        character_counts[input_line[end]] += 1
        character_counts[input_line[start]] -= 1
        if character_counts[input_line[start]] == 0:
            del character_counts[input_line[start]]

        if len(character_counts) == args.distinct_length:
            print(character_counts)
            return end + 1   # Off by one error. The 7th character is index 6

        start += 1
        end += 1


if __name__ == "__main__":
    print(main())
