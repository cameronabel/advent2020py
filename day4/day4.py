import sys


def part_one(puzzle_input, func):
    valid_passports = 0
    content = []
    with open(puzzle_input, 'r') as f:
        for line in f:
            if line == '\n':
                if content:
                    valid_passports += func(content)
                content = []
            else:
                content.append(line)
    if content:
        valid_passports += func(content)
    return valid_passports
    
    
def is_valid_one(content):
    present_fields = set()
    required_fields = {'ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt'}
    for line in content:
        fields = line.split()
        for field in fields:
            present_fields.add(field[:3])
    try:
        present_fields.remove('cid')
    except Exception:
        pass
    return present_fields == required_fields


def is_valid_two(content):
    present_fields = {}
    for line in content:
        for field in line.strip().split():
            k, v = field.split(':')
            present_fields[k] = v
    if len(present_fields) < 7:
        return False
    try:
        assert 1920 <= int(present_fields['byr']) <= 2002
        assert 2010 <= int(present_fields['iyr']) <= 2020
        assert 2020 <= int(present_fields['eyr']) <= 2030
        if present_fields['hgt'][-2:] == 'cm':
            assert 150 <= int(present_fields['hgt'][:-2]) <= 193
        elif present_fields['hgt'][-2:] == 'in':
            assert 59 <= int(present_fields['hgt'][:-2]) <= 76
        else:
            return False
        assert present_fields['hcl'][0] == '#' and len(present_fields['hcl']) == 7
        for char in present_fields['hcl'][1:]:
            assert char in '0123456789abcdef'
        assert present_fields['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
        assert len(present_fields['pid']) == 9 and int(present_fields['pid']) <= 999999999
    except Exception:
        return False
    return True


if __name__ == '__main__':
    print(part_one(sys.argv[1], is_valid_one))
    print(part_one(sys.argv[1], is_valid_two))