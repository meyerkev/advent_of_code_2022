

def parse_line(line):
    pair = []
    for part in line.split(','):
        pair.append([int(x) for x in part.split('-')])

    return pair


def detect_partial_overlap(pair):
    # (2, 3) (3, 4) -> True
    # 3 >= 3 and 2 <= 4
    if pair[0][1] >= pair[1][0] and pair[0][0] <= pair[1][1]:
        return True
    # (3, 4) (2, 3) -> True
    # 3 >= 3 and 4 <= 2
    if pair[0][0] <= pair[1][1] and pair[0][1] >= pair[1][0]:
        return True
    return False


def main():
    with open('input.txt') as f:
        count = 0
        for line in f:
            pair = parse_line(line)
            if detect_partial_overlap(pair):
                count += 1
        return count


if __name__ == "__main__":
    print(main())
