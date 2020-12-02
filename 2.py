# https://adventofcode.com/2020/day/2

from typing import List, Optional


def read_valid_input(path: str, val_func) -> List[Optional[str]]:
    with open(path) as f:
        return [parse_line(line, val_func) for line in f.readlines() if parse_line(line, val_func)]


def parse_line(line: str, val_func) -> Optional[str]:
    rule, pw = line.strip().split(': ')

    nums, char = rule.split(' ')
    a, b = nums.split('-')

    if val_func(char, int(a), int(b), pw):
        return pw
    return None


def is_valid_part_one(char: str, min: int, max: int, pw: str) -> bool:
    return min <= pw.count(char) <= max


def is_valid_part_two(char: str, i: int, j: int, pw: str) -> bool:
    return (pw[i-1] == char and pw[j-1] != char) or (pw[i-1] != char and pw[j-1] == char)


if __name__ == "__main__":
    # 1
    valid_passwords = read_valid_input('res/2.txt', is_valid_part_one)
    print(len(valid_passwords))

    # 2
    valid_passwords = read_valid_input('res/2.txt', is_valid_part_two)
    print(len(valid_passwords))
