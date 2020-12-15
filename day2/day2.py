import sys


def part_one(array):
    """Returns the number of entries wherein the defined character appears
    within the specified number of times in the string
    """
    valid = 0
    for line in array:
        if line[0] <= line[3].count(line[2]) <= line[1]:
            valid += 1
    return valid


def part_two(array):
    """Returns the number of entries wherein the defined character appears
    at exactly one of the the specified indices in the string
    """
    valid = 0
    for line in array:
        first = line[3][line[0] - 1] == line[2]
        second = line[3][line[1] - 1] == line[2]
        valid += first != second
    return valid


def build_array(text):
    """Returns an array of parsed lines from the input text
    Array elements are in the format:
        (min, max, character, string)
    """
    array = []
    with open(text, 'r') as f:
        for line in f:
            _range, char, s = line.strip().split()
            n, m = _range.split('-')
            array.append((int(n), int(m), char[0], s))
    return array


if __name__ == '__main__':
    array = build_array(sys.argv[1])
    print(part_one(array))
    print(part_two(array))
    