
def item_priority(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1

    raise ValueError(f"Invalid character {c}")


def sack_priority(line):
    part1, part2 = set(line[:len(line)//2]), set(line[len(line)//2:])
    matching_item = part1.intersection(part2).pop()
    return item_priority(matching_item)


def main():
    with open('input.txt') as f:
        total_priority = 0
        for line in f:
            total_priority += sack_priority(line.strip())

    return total_priority


if __name__ == "__main__":
    print(main())
