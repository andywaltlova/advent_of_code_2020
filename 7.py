from typing import Dict


def read_rules_to_graph(path) -> Dict[str, Dict[str, int]]:
    with open(path) as f:
        # split to key and values
        rules = [line.strip('\n.').split(' bags contain ')
                 for line in f.readlines()]

    # make dict, split values into lists
    rules = {r[0]: [b.replace(' bags', '').replace(' bag', '').split(' ', 1)
                    for b in r[1].split(', ')]
             for r in rules}

    # make from values dicts with key(color):v(number)
    return {c: {b[1]: int(b[0]) for b in v if b[0].isdigit()} for c, v in rules.items()}


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    # if start not in graph:
    #     return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
    return None


def possible_outer_bags(graph, end):
    res = []
    for color in graph:
        if color != end:
            path = find_path(graph, color, end)
            if path:
                res.append(color)
    return set(res)


def count_needed_bags(graph, start):
    cnt = 0
    for node, n in graph[start].items():
        if n:
            cnt += n + n * count_needed_bags(graph, node)
        else:
            return 1
    return cnt


if __name__ == "__main__":
    b_graph = read_rules_to_graph("res\\7.txt")

    # Part one
    print(len(possible_outer_bags(b_graph, 'shiny gold')))

    # Part two
    print(count_needed_bags(b_graph, 'shiny gold'))
