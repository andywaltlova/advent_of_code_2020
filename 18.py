# https://adventofcode.com/2020/day/18

from operator import add, mul
from math import prod
from collections import deque
import re


def read_expresions(path):
    with open(path) as f:
        exprs = [l.strip() for l in f.readlines()]
    return exprs


def equal_eval(expr, operators={'+': add, '*': mul}):
    expr = deque(expr.split())
    res = int(expr.popleft())
    while expr:
        op, num = expr.popleft(), int(expr.popleft())
        res = operators[op](res, num)
    return res


def add_before(expr):
    # Just means splitting string by '*' and evaluate everything before multiplying
    return prod(map(equal_eval, expr.split("*")))


def evaluate_exp(expresion, inner_f):

    # Find expresion in brackets
    bracket_re = re.compile(r'(\([^()]+\))')
    bracket_e = bracket_re.search(expresion)

    if not bracket_e:
        return inner_f(expresion)

    bracket_e = bracket_e.group(1)
    brackets_result = inner_f(bracket_e.strip('()'))

    # evaluate recursively until no brackets are found
    new_e = expresion.replace(bracket_e, str(brackets_result))
    return evaluate_exp(new_e, inner_f)


if __name__ == '__main__':
    expresions = read_expresions('res//18.txt')
    first = sum(evaluate_exp(line, equal_eval) for line in expresions)
    print(first)

    second = sum(evaluate_exp(line, add_before) for line in expresions)
    print(second)
