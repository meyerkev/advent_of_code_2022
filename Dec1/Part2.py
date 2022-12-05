#!/bin/env python3

def main():
    with open('input.txt') as f:
        elves = []
        elf_total = 0
        for line in f:
            line = line.strip()
            if not line:
                elves.append(elf_total)
                elf_total = 0
                continue
            elf_total += int(line)
        elves.sort()
        return sum(elves[-3:])


if __name__ == "__main__":
    print(main())
