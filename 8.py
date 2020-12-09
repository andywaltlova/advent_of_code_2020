# https://adventofcode.com/2020/day/8
from copy import deepcopy


def read_input(path):
    with open(path) as f:
        lines = [line.strip().split(' ')for line in f.readlines()]
    return [(l[0], int(l[1])) for l in lines]


def detect_infinite_loop(inpt):
    visited, acc, i = set(), 0, 0
    while i != len(inpt):
        if i in visited or 0 > i or i >= len(inpt):
            return True, acc
        op = inpt[i][0]
        visited.add(i)
        if op == 'jmp':
            i += inpt[i][1]
            continue
        elif op == 'acc':
            acc += inpt[i][1]
        i += 1
    return False, acc


def repair_loop(inpt):
    to_try = [i for i, v in enumerate(inpt) if v[0] != 'acc']

    def switch_f(op, offset): return [
        'nop', offset] if op == 'jmp' else ['jmp', offset]

    not_okay, acc = detect_infinite_loop(inpt)
    while not_okay:
        new_inpt = deepcopy(inpt)
        i = to_try.pop()
        new_inpt[i] = switch_f(*new_inpt[i])
        not_okay, acc = detect_infinite_loop(new_inpt)
    return acc


if __name__ == "__main__":
    inpt = read_input('res//8.txt')
    # Part one
    print(detect_infinite_loop(inpt)[1])

    # Part two
    print(repair_loop(inpt))
