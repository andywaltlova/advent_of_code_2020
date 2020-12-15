# https://adventofcode.com/2020/day/14
from itertools import product


def read_input(path: str):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]
    return list(map(lambda x: x.split(' = '), lines))


def binary_to_decimal(n):
    return int(n, 2)

###############################################################################


def decoder_version_1(input):
    res = {}
    mask = inpt[0][0]
    for c, v in input:
        if c == 'mask':
            mask = v
            continue

        n = (f'{int(v):036b}')
        res[int(c.replace('mem', '')[1:-1])] = apply_mask1(n, mask)
    return sum(list(res.values()))


def apply_mask1(k, mask):
    to_change = [(i, n) for i, n in enumerate(mask) if n.isdigit()]
    for i, n in to_change:
        k = k[:i] + f'{n}' + k[i + 1:]
    return binary_to_decimal(k)


###############################################################################


def decoder_version_2(inpt):
    res = {}
    for c, v in inpt:
        if c == 'mask':
            mask = v
            continue

        n = (f'{int(c.replace("mem", "")[1:-1]):036b}')
        apply_mask2(v, n, mask, res)
    return sum(list(res.values()))


def apply_mask2(v, k, mask, res):
    # replace all 1
    to_change = [(i, n) for i, n in enumerate(mask) if n == '1']
    for i, n in to_change:
        k = k[:i] + f'{n}' + k[i + 1:]

    # take care of floating bits
    f_bits_i = [i for i, n in enumerate(mask) if n == 'X']
    perms = list(product(range(2), repeat=len(f_bits_i)))

    for p in perms:
        new_k = list(k)
        for ip, ib in enumerate(f_bits_i):
            new_k[ib] = p[ip]
        res[binary_to_decimal("".join(map(str, new_k)))] = int(v)


if __name__ == "__main__":
    inpt = read_input('res\\14.txt')

    print(decoder_version_1(inpt))
    print(decoder_version_2(inpt))
