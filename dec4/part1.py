

def parse_line(line):
    pair = []
    for part in line.split(','):
        pair.append([int(x) for x in part.split('-')])

    return pair


def detect_overlap(pair):
    if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
        return True
    elif pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
        return True
    return False
        

def main():
    with open('input.txt') as f:
        count = 0
        for line in f:
            pair = parse_line(line)
            if detect_overlap(pair):
                count += 1
        return count
            

if __name__ == "__main__":
    print(main())