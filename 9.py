# https://adventofcode.com/2020/day/9

def load_nums(file):
    with open(file) as f:
        lines = [int(line.strip()) for line in f.readlines()]
    return lines


def sum_exists(nums, k):
    for n in nums:
        if (k - n) in nums:
            return True
    return False


def find_n(nums, p_size):
    start, i = 0, p_size
    preamble = nums[start:i]
    while sum_exists(preamble, nums[i]):
        start, i = start + 1, i + 1
        preamble = nums[start:i]
    return nums[i]


def find_encryption_weakness(nums, k):
    start = 0
    while start < len(nums):
        res, s = [], 0
        for n in nums[start:]:
            res.append(n)
            s += n
            if s > k:
                break
            elif s == k:
                return min(res) + max(res)
        start += 1
    return None


if __name__ == "__main__":
    inpt = load_nums("res//9.txt")

    # Part one
    k = find_n(inpt, 25)
    print(k)

    # Part two
    print(find_encryption_weakness(inpt, k))
