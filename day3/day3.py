import sys


def part_one(array, over, down):
    """Returns the number of trees encountered in the given array at the given slope"""
    trees = 0
    col = 0
    for line in array[down::down]:
        col += over
        if col >= len(line):
            col -= len(line)
        if line[col] == '#':
            trees += 1
    return trees


def part_two(array, slopes):
    """Returns the product of trees for the given array and each given slope"""
    trees = 1
    for slope in slopes:
        trees *= part_one(array, slope[0], slope[1])
    return trees


def build_array(text):
    """Returns an array representing the hill in the given text source"""
    with open(text, 'r') as f:
        array = [line.strip() for line in f]
    return array


if __name__ == '__main__':
    array = build_array(sys.argv[1])
    print(part_one(array, 3, 1))
    slopes = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    print(part_two(array, slopes))
