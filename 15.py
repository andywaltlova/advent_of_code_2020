# https://adventofcode.com/2020/day/15

import time


def elven_game(start_nums, end):
    res = {n: (None, i) for i, n in enumerate(start_nums, start=1)}
    turn = len(start_nums)+1

    spoken = 0
    while turn != end:
        if spoken in res:
            second_last, last = res[spoken]
            res[spoken] = last, turn
            spoken = turn - last
        else:
            res[spoken] = None, turn
            spoken = 0
        turn += 1
    return spoken


if __name__ == "__main__":
    inpt = [0, 1, 4, 13, 15, 12, 16]

    # Part 1
    start_time = time.time()
    nth = 2020
    print(elven_game(inpt, nth))
    print(f"--- {(time.time() - start_time)} seconds ---")

    # Part 2
    start_time = time.time()
    nth = 30000000
    print(elven_game(inpt, nth))
    print(f"--- {(time.time() - start_time)} seconds ---")
