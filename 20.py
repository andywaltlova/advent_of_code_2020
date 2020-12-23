# https://adventofcode.com/2020/day/20
# Inspired by: https://github.com/Diderikdm/Advent-of-Code-2020/blob/main/day%2020%20-%20part%201%20%26%202

from math import prod


def load_tiles(path):
    with open(path) as f:
        lines = f.read().strip('\n').split('\n\n')
        tiles = {int(x.split(':\n')[0].split(' ')[1])
                     : x.split(':\n')[1] for x in lines}
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

    return flips, borders, res, prod([a for a, b in res.items() if b == 4])


def find_image_start(flips, borders, adj_b):
    picture = [[[] for _ in range(int(len(inpt.keys())**0.5))]
               for _ in range(int(len(inpt.keys())**0.5))]

    # find corner of image (top left)
    for k in flips:
        if adj_b[k] == min(adj_b.values()):
            others = sum([w for q, w in borders.items() if k != q], [])
            for x in flips[k]:
                if ''.join([d[-1] for d in x]) in others and x[-1] in others:
                    picture[0][0], used_tile = x, [k]
                    break
    return picture, used_tile


def construct_image(picture, used, flips):
    # rest of image
    for y in range(len(picture)):
        # Find matching tiles for first row
        if y == 0:
            for x in range(1, len(picture)):
                for key in flips.keys():
                    if key not in used:
                        for i in range(len(flips[key])):
                            if ''.join([t[0] for t in flips[key][i]]) == ''.join([j[-1] for j in picture[y][x-1]]):
                                picture[y][x] = flips[key][i]
                                used.append(key)

        else:
            for x in range(len(picture[0])):
                for key in flips.keys():
                    if key not in used:
                        for i in range(len(flips[key])):
                            if flips[key][i][0] == picture[y-1][x][-1]:
                                picture[y][x] = flips[key][i]
                                used.append(key)
    # remove outer borders
    for y in range(len(picture)):
        for x in range(len(picture)):
            picture[y][x] = [f[1:-1] for f in picture[y][x][1:-1]]

    # flatten image
    return [''.join([z[x] for z in y]) for y in picture for x in range(len(y[0]))]


def find_dragons(image):
    dragon = ["                   # ",
              " #    ##    ##    ###",
              "  #  #  #  #  #  #   "]
    idx = []
    for y in range(len(dragon)):
        for x in range(len(dragon[0])):
            if dragon[y][x] == '#':
                idx.append([x, y])
    tot = 0
    for rot in [image,
                turn(image, 1),
                turn(image, 2),
                turn(image, 3),
                [x[::-1] for x in image],
                turn([x[::-1] for x in image], 1),
                turn([x[::-1] for x in image], 2),
                turn([x[::-1] for x in image], 3)]:
        for y in range(len(image)-len(dragon)):
            for x in range(len(rot[y])-len(dragon[0])):
                if all([rot[y+j][x+i] == '#' for i, j in idx]):
                    tot += len([z for z in ''.join(dragon) if z == '#'])
    return len([z for z in ''.join(image) if z == '#'])-tot


if __name__ == "__main__":
    inpt = load_tiles('res/20.txt')

    # Part 1
    flips, borders, adj_b, part1 = part_1(inpt)
    print(part1)

    # Part 2 - Image needs to be constructed (because i used only borders in part 1)
    picture, used = find_image_start(flips, borders, adj_b)
    image = construct_image(picture, used, flips)
    print(find_dragons(image))
