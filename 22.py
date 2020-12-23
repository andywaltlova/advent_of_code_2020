# https://adventofcode.com/2020/day/22
from collections import deque
from copy import deepcopy


def load_decks(path):
    with open(path) as f:
        lines = [l.strip() for l in f.readlines()]

    index = lines.index('')
    decks = [lines[:index], lines[index + 1:]]
    p1, p2 = [list(map(int, d[1:])) for d in decks]
    return p1, p2


def play1(p1, p2):
    while p1 and p2:
        p1_t, p2_t = p1.popleft(), p2.popleft()

        if p1_t > p2_t:
            p1.append(p1_t)
            p1.append(p2_t)
        else:
            p2.append(p2_t)
            p2.append(p1_t)

    winner = p1 if p1 else p2
    return count_score(winner)


def play2(p1, p2):
    seen = set()

    while p1 and p2:
        # to stop recursion
        if (state := (tuple(p1), tuple(p2))) in seen:
            return 1, p1
        seen.add(state)

        (p1_t, *p1), (p2_t, *p2) = p1, p2

        # sub game
        if len(p1) >= p1_t and len(p2) >= p2_t:
            winner, _ = play2(p1[:p1_t], p2[:p2_t])
        # Higher card
        else:
            winner = 1 if p1_t > p2_t else 2

        # Give winner cards
        if winner == 1:
            p1.extend((p1_t, p2_t))
        else:
            p2.extend((p2_t, p1_t))

    return (1, p1) if p1 else (2, p2)


def count_score(deck):
    score = 0
    for i, card in enumerate(reversed(deck), start=1):
        score += i*card
    return score


if __name__ == "__main__":
    p1, p2 = load_decks('res/22.txt')

    print(play1(deque(p1), deque(p2)))

    print(count_score(play2(p1, p2)[1]))
