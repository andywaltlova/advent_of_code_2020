# https://adventofcode.com/2020/day/6


from typing import List, Set


def read_groups(path):
    res = []
    with open(path) as f:
        lines = f.readlines()
        lines.append('\n')

        group = ''
        for line in lines:
            if line == '\n':
                res.append(group.strip('\n'))
                group = ''
            group += line
    return res


def intersect_persons_answers(group: str):
    persons = group.split('\n')
    p_set = [set(p) for p in persons]
    return len(p_set[0].intersection(*p_set[1:]))


if __name__ == "__main__":
    groups = read_groups('res/6.txt')

    # Part one
    sum_a = sum([len(set(g.replace('\n', ''))) for g in groups])
    print(sum_a)

    # Part two
    sum_uniq_a = sum([intersect_persons_answers(g) for g in groups])
    print(sum_uniq_a)
