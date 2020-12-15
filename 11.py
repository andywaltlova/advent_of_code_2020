# https://adventofcode.com/2020/day/11
from typing import Dict, Tuple
from copy import deepcopy


def load_seats(file):
    seats = {}
    with open(file) as f:
        i = 1
        for line in f.readlines():
            j = 1
            for seat in line.strip():
                seats[(i, j)] = seat
                j += 1
            i += 1
    return seats


def get_seats_to_change(seats: Dict[Tuple[int, int], str], part):
    to_change = []
    for k, v in seats.items():
        x, y = k
        # part one
        adjacent = [(x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1),
                    (x + 1, y), (x + 1, y - 1), (x, y - 1), (x - 1, y - 1)]

        # part two
        direction = [(-1, 0), (-1, +1), (0, +1), (+1, +1),
                     (+1, 0), (+1, -1), (0, -1), (-1, -1)]

        seat = seats.get((x, y))

        if seat == 'L':
            if part == 1:
                all_adj_empty = [seats.get((i, j)) in 'L.' for i,
                                 j in adjacent if seats.get((i, j))]
            else:
                all_adj_empty = [find_nearest_seat(
                    (x, y), (i, j), seats) == 'L' for i, j in direction if find_nearest_seat((x, y), (i, j), seats)]

            if all(all_adj_empty):
                to_change.append((x, y))

        elif seat == '#':
            if part == 1:
                count_occup = [seats.get((i, j)) == '#' for i,
                               j in adjacent if seats.get((i, j))]
            else:
                count_occup = [find_nearest_seat(
                    (x, y), (i, j), seats) == '#' for i, j in direction if find_nearest_seat((x, y), (i, j), seats)]

            lim = 4 if part == 1 else 5
            if count_occup.count(True) >= lim:
                to_change.append((x, y))
        else:
            continue

    return to_change


def change_seats(seats, part):
    while to_change := get_seats_to_change(seats, part):
        new_seats = deepcopy(seats)
        for seat in to_change:
            new_seats[seat] = swap(seats[seat])
        seats = new_seats

    return list(seats.values()).count('#')


def swap(v):
    return 'L' if v == '#' else '#'


def find_nearest_seat(start, direction, seats):
    x, y = start
    x, y = x + direction[0], y+direction[1]
    while seats.get((x, y)) == '.':
        x, y = x + direction[0], y + direction[1]
    return seats.get((x, y))


if __name__ == "__main__":
    seats = load_seats("res\\11.txt")

    # Part one
    print(change_seats(seats, 1))

    # Part two
    print(change_seats(seats, 2))
