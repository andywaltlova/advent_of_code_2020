from itertools import product
import operator

# Credit: https://github.com/cberigan/advent-of-code-2020/blob/master/day17.py
# I added comments just for understand how to do something similar in the future, I never used itertools or operator module


def run_cycles(dimensions):
    with open('res//17.txt') as f:
        curr_state = [l.strip() for l in f.readlines()]

    state = {}
    # load state into dictionary (keys are coordinates)
    for y in range(0, len(curr_state)):
        for x in range(0, len(curr_state[0])):
            p = [x, y] + [0] * (dimensions-2)
            state[tuple(p)] = curr_state[y][x]

    cycles = 6
    for i in range(0, cycles):
        # create space to view
        for p in list(state):

            # Product creates cartesian product (like nested loops)
            # e.g product([-1, 0, 1],repeat=2) creates:

            # [(-1, -1), (-1, 0), (-1, 1),
            #  (0, -1), (0, 0), (0, 1),
            # (1, -1), (1, 0), (1, 1)]

            for step in product([-1, 0, 1], repeat=dimensions):
                # operator.add just simulates adding (x+y)
                view = tuple(map(operator.add, p, step))
                if view not in state:
                    state[view] = '.'

        state_next = {}
        for p, v in state.items():

            # count active neighbour cubes
            count = 0
            for step in product([-1, 0, 1], repeat=dimensions):
                test = tuple(map(operator.add, p, step))
                if p == test or test not in state:
                    continue
                if state[test] == '#':
                    count += 1

            # Change states
            if v == '#' and (count == 3 or count == 2):
                state_next[p] = '#'
            elif v == '.' and count == 3:
                state_next[p] = '#'
            else:
                state_next[p] = '.'

        state = state_next

    print(count_total_active(state))


def count_total_active(state):
    total_active = 0
    for p, v in state.items():
        if v == '#':
            total_active += 1
    return total_active


run_cycles(3)
run_cycles(4)
