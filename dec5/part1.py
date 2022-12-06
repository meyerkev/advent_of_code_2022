import re


def parse_box_line(line):
    index = 0
    while index < len(line):
        blob = line[index:index+4]
        if len(blob) < 3:
            return
        if blob[1].isspace():
            yield None
        else:
            yield blob[1]
        index += 4


def generate_stacks(lines):
    stacks = []
    for index, line in enumerate(lines):
        if not '[' in line:
            break
        stack_adds = [x for x in parse_box_line(line)]

        if len(stacks) < len(stack_adds):
            for i in range(len(stack_adds) - len(stacks)):
                stacks.append([])

        for i, stack_add in enumerate(stack_adds):
            if stack_add:
                stacks[i].append(stack_add)

    for stack in stacks:
        stack.reverse()

    index += 2

    return stacks, index


def parse_move_line(line):
    m = re.match(
        r'move (?P<boxes>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)', line)
    d = {k: int(v) for k, v in m.groupdict().items()}
    d['from_stack'] -= 1
    d['to_stack'] -= 1
    return d


def move(stacks, boxes, from_stack, to_stack):
    for i in range(boxes):
        stacks[to_stack].append(stacks[from_stack].pop())


def main():
    with open("input.txt") as f:
        lines = f.readlines()

    stacks, index = generate_stacks(lines)

    for index in range(index, len(lines)):
        line = lines[index]
        line = line.strip()
        move_obj = parse_move_line(line)
        move(stacks, **move_obj)

    return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    print(main())
