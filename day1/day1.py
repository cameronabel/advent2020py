import sys


def part_one(nums, target):
    for n in nums:
        m = target - n
        if m in nums:
            return n * m

        
def part_two(nums, target):
    for num in nums:
        new_target = target - num
        result = part_one(nums, new_target)
        if result is not None:
            return num * result

    
def build_array(text):
    with open(text, 'r') as f:
        nums = {int(line.strip()) for line in f}
    return nums

            
if __name__ == '__main__':
    array = build_array(sys.argv[1])
    print(part_one(array, 2020))
    print(part_two(array, 2020))
