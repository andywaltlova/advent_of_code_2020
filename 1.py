# https://adventofcode.com/2020/day/1


from typing import List, Optional, Tuple


def read_input(path: str) -> List[int]:
    with open(path) as f:
        lines = [int(line.strip()) for line in f.readlines()]
    return lines


def find_two_nums_with_sum(numbers: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    a_len = len(numbers)
    for a in range(0, a_len-1):
        for b in range(a+1, a_len):
            if numbers[a] + numbers[b] == target_sum:
                return numbers[a], numbers[b]
    return None


def find_three_nums_with_sum(numbers: List[int], target_sum: int) -> Optional[Tuple[int, int, int]]:
    a_len = len(numbers)
    numbers.sort()

    for i in range(0, a_len - 2):

        l_bound = i + 1
        r_bound = a_len - 1

        a = numbers[i]
        while l_bound < r_bound:
            b = numbers[l_bound]
            c = numbers[r_bound]

            if a + b + c == target_sum:
                return a, b, c
            elif a + b + c > target_sum:
                r_bound -= 1
            else:
                l_bound += 1

    return None


if __name__ == "__main__":
    path = 'res/1.txt'
    nums = read_input(path)

    # First-part
    res1 = find_two_nums_with_sum(nums, 2020)
    assert res1
    print(res1[0] * res1[1])

    # Second-part
    res2 = find_three_nums_with_sum(nums, 2020)
    assert res2
    print(res2[0] * res2[1] * res2[2])
