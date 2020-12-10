# https://adventofcode.com/2020/day/10
from math import prod


def load_nums(file):
    with open(file) as f:
        lines = [int(line.strip()) for line in f.readlines()]
    return sorted(lines)


def count_differences(nums):
    res = {1: 1, 2: 0, 3: 1}
    for i in range(len(nums)-1):
        a, b = nums[i], nums[i+1]
        res[b-a] += 1
    return res[1] * res[3]


def three_fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 2
    return three_fib(n-1) + three_fib(n-2) + three_fib(n-3)


def lenghts_of_consecutive_parts(nums):
    chunks, chunk = [], []
    prev = None
    for el in nums:
        if not prev:
            prev = el
            chunk.append(el)
            continue

        if el == prev + 1:
            chunk.append(el)
        else:
            chunks.append(chunk)
            chunk = [el]
        prev = el
    chunks.append(chunk)
    return list(map(len, chunks))


def count_of_arrangements(nums):
    return prod(list(map(three_fib, lenghts_of_consecutive_parts(nums))))


if __name__ == "__main__":
    nums = load_nums('res//10.txt')

    # Part one
    print(count_differences(nums))

    # Part two
    print(count_of_arrangements([0] + nums))
