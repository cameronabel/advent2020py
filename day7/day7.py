import sys


def part_one(puzzle_input):
    bags = {}
    total = 0
    with open(puzzle_input, 'r') as f:
        for line in f:
            bag, contents = line.strip().split('contain')
            bags[bag.rsplit(' ', 2)[0]] = [inner.split(' ', 2)[2].rsplit(' ', 1)[0] for inner in contents.split(',')]
    for color in bags:
        if bag_check(color, bags):
            total += 1
    return total

def bag_check(color, bags):
    if 'shiny gold' in bags[color]:
        return True
    elif 'other' in bags[color]:
        return False
    else:
        return any([bag_check(bag, bags) for bag in bags[color]])


def part_two(puzzle_input):
    bags = {}
    with open(puzzle_input, 'r') as f:
        for line in f:
            bag, contents = line.strip().split('contain')
            bags[bag.rsplit(' ', 2)[0]] = [inner.strip().rsplit(' ', 1)[0] for inner in contents.split(',')]

    return bag_check_two('shiny gold', bags)


def bag_check_two(color, bags):
    total = 1
    if bags[color][0] != 'no other':
        for bag in bags[color]:
            total += int(bag.split(' ', 1)[0]) * bag_check_two(bag.split(' ', 1)[1], bags)
    return total


if __name__ == '__main__':
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))
    