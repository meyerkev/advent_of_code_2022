#!/bin/env python3

def main():
    with open('input.txt') as f:
        max_total = 0
        elf_total = 0
        for line in f:
            line = line.strip()
            if not line:
                max_total = max(elf_total, max_total)
                elf_total = 0
                continue
            elf_total += int(line)

        max_total = max(elf_total, max_total)
        return max_total


if __name__ == "__main__":
    print(main())
