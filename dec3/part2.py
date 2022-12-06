
def item_priority(c):
    if 'A' <= c <= 'Z':
        return ord(c) - ord('A') + 27
    if 'a' <= c <= 'z':
        return ord(c) - ord('a') + 1

    raise ValueError(f"Invalid character {c}")


def three_lines(f):
    lines = []
    while line := f.readline():
        lines.append(line.strip())
        if len(lines) == 3:
            yield lines
            lines = []


def badge_priority(group):
    set1, set2, set3 = set(group[0]), set(group[1]), set(group[2])
    matching_item = set1.intersection(set2).intersection(set3).pop()
    return item_priority(matching_item)


def main():
    with open('input.txt') as f:
        total_priority = 0
        for group in three_lines(f):
            total_priority += badge_priority(group)

    return total_priority


if __name__ == "__main__":
    print(main())
