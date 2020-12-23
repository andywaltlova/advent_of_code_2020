# https://adventofcode.com/2020/day/21

def read_input(path):
    with open(path) as f:
        return [l.strip() for l in f.readlines()]


def part_1(inpt):
    alrgs, ingrs = {}, []
    for food in inpt:
        ins, als = food.rstrip(")").split("(contains ")
        ingr = ins.split()
        ingrs.append(ingr)

        for a in als.split(", "):
            if a not in alrgs:
                alrgs[a] = set(ingr)
            else:
                # intersection
                alrgs[a] &= set(ingr)

    all_alrgs = set(v for a in alrgs.values() for v in a)
    return alrgs, sum(i not in all_alrgs for ingr in ingrs for i in ingr)


def part_2(alrgs):
    # find set with one element
    r = next(list(v) for v in alrgs.values() if len(v) == 1)
    while r:
        r += list(remove_a_from_all_alrgs(r.pop(), alrgs))

    sorted_a = sorted((k, v) for k, v in alrgs.items())
    return ','.join(str(i.pop()) for _, i in sorted_a)


def remove_a_from_all_alrgs(a, alrgs):
    one_sets = set()
    for k in alrgs:
        if len(alrgs[k]) > 1 and a in alrgs[k]:
            alrgs[k].remove(a)
            if len(alrgs[k]) == 1:
                one_sets |= alrgs[k]
    return one_sets


if __name__ == "__main__":
    inpt = read_input('res/21.txt')
    alrgs, part1 = part_1(inpt)

    print(part1)
    print(part_2(alrgs))
