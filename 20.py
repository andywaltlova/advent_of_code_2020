# https://adventofcode.com/2020/day/20
from math import prod


def load_tiles(path):
    with open(path) as f:
        lines = f.read().strip('\n').split('\n\n')
        tiles = {int(x.split(':\n')[0].split(' ')[1])                 : x.split(':\n')[1] for x in lines}
    return {k: v.split('\n') for k, v in tiles.items()}


def turn(lines, no_turns):
    for _ in range(no_turns):
        turned = [''.join([z[y] for z in reversed(lines)])
                  for y in range(len(lines))]
        lines = turned
    return lines


def part_1(inpt):
    borders, flips = {}, {}
    for ID, tile in inpt.items():

        # all possible flips and rotations of tile
        flips[ID] = [tile,
                     turn(tile, 1),
                     turn(tile, 2),
                     turn(tile, 3),
                     [x[::-1] for x in tile],
                     turn([x[::-1] for x in tile], 1),
                     turn([x[::-1] for x in tile], 2),
                     turn([x[::-1] for x in tile], 3)]

        # just right borders
        borders[ID] = [x[0] for x in flips[ID]]

    res = {}
    for ID, border in borders.items():
        # keep only borders, that have matching one in different tile, save to res its count
        # corners should have 4 (two matching sides and their fliped versions)
        res[ID] = len([b for b in border if any(
            [b in border_a for ID_a, border_a in borders.items() if ID != ID_a])])

    return prod([a for a, b in res.items() if b == 4])


if __name__ == "__main__":
    inpt = load_tiles('res/20.txt')
    print(part_1(inpt))
