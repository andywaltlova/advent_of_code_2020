# https://adventofcode.com/2020/day/19

# Credit for solution : https://github.com/BastiHz/Advent_of_Code/blob/main/2020/day_19.py
# Added comments for myself, really inspiring solution, especially solution of part 2
import itertools


def read_input(path):
    with open(path) as f:
        lines = [l.strip() for l in f.readlines()]
    index = lines.index('')
    rules, messages = [lines[:index], lines[index + 1:]]

    rules = {int(r.split(': ')[0]):
             list(map(lambda x: [int(r) if r.isdigit() else r.strip('"')
                                 for r in x.split()], r.split(': ')[1].split(' | ')))
             for r in rules}
    rules = {k: (v if isinstance(v[0][0], int) else v[0][0])
             for k, v in rules.items()}
    return rules, messages


# Recursive search with memorization. Part 1 is easy, that I completed with same approach
def resolve_rules(rules, cache, key=0):
    if key in cache:
        return cache[key]

    rule = rules[key]
    if isinstance(rule, str):
        cache[key] = rule
        return rule

    res = []
    # opt = option in rule (some rules have more options)
    for opt in rule:
        temp = [resolve_rules(rules, cache, next_i) for next_i in opt]
        res.extend("".join(x) for x in itertools.product(*temp))
    cache[key] = res
    return res


def part_1(rules, messages):
    valid_messages = set(resolve_rules(rules, {}))
    return sum(message in valid_messages for message in messages)


# Part 2 was like magic to me, but after explanation it makes sense
"""
Explanation for part 2:

- Rule 8 returns these:
  (42), (42, 42), (42, 42, 42), ...
  And rule 11 returns these:
  (42, 31), (42, 42, 31, 31), (42, 42, 42, 31, 31, 31), ...

- The loopy part comes in the second half of the rules. That means
  [42] or [42, 31] are already resolved when it is reached.

- In the test rules and challenge rules rule 0 points directly
  to 8 and 11 IN THIS ORDER. That means every valid rule must follow
  one of these patterns:
  1. left + left:   42, 42, 31
  2. left + right:  42, 42 * x, 31 * x
  3. right + left:  42 * x, 42, 31
  4. right + right: 42 * x, 42 * y, 31 * y
  They have in common that the left part is all 42, the right part
  is all 31 and the number of 31 is less than the number of 42.

- Remember: Solve the challenge for the rules given, not any
  general rules! Start by resolving only rules 31 and 42.
  Then check the patterns.

- Complication: 42 and 31 have many possibilities. But both are always
  the same length. I can split each message into n-character words.
"""


def part_2(rules, messages):

    # Replacement defined in task assignment
    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    # share the cache for both searches
    rule_cache = {}
    r_31 = set(resolve_rules(rules, rule_cache, 31))
    r_42 = set(resolve_rules(rules, rule_cache, 42))

    len_31 = {len(x) for x in r_31}
    len_42 = {len(x) for x in r_42}
    len_both = len_31 | len_42
    assert len(len_both) == 1

    sum_valid = 0
    word_len = len_both.pop()
    for m in messages:
        words = [m[0+i:word_len+i] for i in range(0, len(m), word_len)]
        n_words = len(words)

        n_31 = 0
        for word in reversed(words):
            if word in r_31:
                n_31 += 1
            else:
                break
        if 0 < n_31 < n_words/2 and all(word in r_42 for word in words[:-n_31]):
            sum_valid += 1

    return sum_valid


if __name__ == "__main__":
    rules, messages = read_input("res/19.txt")
    print(part_1(rules, messages))
    print(part_2(rules, messages))
