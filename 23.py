# https://adventofcode.com/2020/day/23

def load_cups(inpt):
    inpt = str(inpt)
    # linked list in dict (cup:next_cup)
    return int(inpt[0]), {int(n): (int(inpt[i+1]) if i+1 < len(inpt) else int(inpt[0])) for i, n in enumerate(inpt)}


def load_cups_part2(inpt):
    first, cups = load_cups(inpt)
    inpt = list(map(int, list(str(inpt))))

    cups[inpt[len(inpt)-1]] = max(inpt) + 1
    for k in range(max(inpt)+1, 1000000):
        cups[k] = k+1
        cups[1000000] = inpt[0]
    return first, cups


def shift_cups(current, cups):
    one = cups[current]
    two = cups[one]
    three = cups[two]

    picked_up = one, two, three

    # Find destination
    dest = current - 1
    if dest < 1:
        dest = max(cups.keys())
    while dest in picked_up:
        dest -= 1
        if dest < 1:
            dest = max(cups.keys())

    # change pointers
    cups[current] = cups[three]
    cups[three] = cups[dest]
    cups[dest] = one


def part_1_labels(cups):
    current = 1
    res = ''
    while len(res) < len(cups)-1:
        res += str(cups[current])
        current = cups[current]
    return res


def play_game(inpt, rounds, part):
    current, cups = load_cups(inpt) if part == 1 else load_cups_part2(inpt)

    rnd = 1
    for _ in range(rounds):
        if rnd != 1:
            current = cups[current]
        shift_cups(current, cups)
        rnd += 1

    return part_1_labels(cups) if part == 1 else cups[1] * cups[cups[1]]


if __name__ == "__main__":

    # part one
    print(play_game(653427918, 100, 1))

    # part two
    print(play_game(653427918, 10000000, 2))
