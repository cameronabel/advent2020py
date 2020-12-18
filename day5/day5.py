import sys


def part_one(puzzle_input):
    high_seat = 0
    with open(puzzle_input, 'r') as f:
        for bpass in f:
            row = decode_bsp(bpass[:7], 127)
            col = decode_bsp(bpass[7:], 7)
            seat = row * 8 + col
            if seat > high_seat:
                high_seat = seat
    return high_seat


def decode_bsp(s, high):
    low = 0
    for char in s:
        if char in 'FL':
            high = (low + high) // 2
        elif char in 'BR':
            low = int((low + high) / 2) + ((low + high) % 2 > 0)
    return low


def part_two(puzzle_input):
    seats = {i: True for i in range(0, 981)}
    with open(puzzle_input, 'r') as f:
        for bpass in f:
            row = decode_bsp(bpass[:7], 127)
            col = decode_bsp(bpass[7:], 7)
            seat = row * 8 + col
            del seats[seat]
    return max(seats.keys())


if __name__ == '__main__':
    print(part_one(sys.argv[1]))
    print(part_two(sys.argv[1]))
