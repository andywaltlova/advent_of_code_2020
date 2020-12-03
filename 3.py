# https://adventofcode.com/2020/day/3
from math import prod


def read_input(path: str):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def traverse(down, side, map):
    width = len(map[0]) - 1
    length = len(map) - 1

    trees = 0
    row, col = down, side
    while row <= length:
        if map[row][col] == '#':
            trees += 1
        row, col = row+down, col+side

        # if needed, expand the map to the side
        if col > width:
            col = (col - width) - 1

    return trees


if __name__ == "__main__":
    path = 'res/3.txt'

    test_m = ['..##.......',
              '#...#...#..',
              '.#....#..#.',
              '..#.#...#.#',
              '.#...##..#.',
              '..#.##.....',
              '.#.#.#....#',
              '.#........#',
              '#.##...#...',
              '#...##....#',
              '.#..#...#.#'
              ]

    # part one
    map = read_input(path)
    trees = traverse(1, 3, map)
    print(trees)

    # part two
    slopes = [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]
    trees = [traverse(d, s, map) for d, s in slopes]
    print(prod(trees))
