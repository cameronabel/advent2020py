import sys


def part_one(puzzle_input):
    total = 0
    content = []
    with open(puzzle_input, 'r') as f:
        for line in f:
            if line == '\n':
                if content:
                    chars = set()
                    for person in content:
                        for char in person.strip():
                            chars.add(char)
                    total += len(chars)
                content = []
            else:
                content.append(line)
        if content:
            chars = set()
            for person in content:
                for char in person.strip():
                    chars.add(char)
            total += len(chars)
    return total


def part_two(puzzle_input):
    total = 0
    content = []
    with open(puzzle_input, 'r') as f:
        for line in f:
            if line == '\n':
                if content:
                    chars = set('abcdefghijklmnopqrstuvwxyz')
                    for person in content:
                        indiv = set(person.strip())
                        chars = chars.intersection(indiv)
                    total += len(chars)
                content = []
            else:
                content.append(line)
        if content:
            chars = set('abcdefghijklmnopqrstuvwxyz')
            for person in content:
                indiv = set(person.strip())
                chars = chars.intersection(indiv)
            total += len(chars)

    return total


if __name__ == '__main__':
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))