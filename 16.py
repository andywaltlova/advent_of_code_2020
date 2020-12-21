from math import prod


def read_input(path: str):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]
    res = []
    tmp = []
    for l in lines:
        if l == '':
            res.append(tmp)
            tmp = []
        else:
            tmp.append(l)
    res.append(tmp)
    return res


def parse_tickets(tickets):
    return [list(map(int, t.split(','))) for t in tickets[1:]]


def parse_fields(fields):
    fields = [f.split(': ') for f in fields]
    fields = {k: [range(int(r.split('-')[0]), int(r.split('-')[1])+1)
                  for r in v.split(' or ')] for k, v in fields}
    return fields


def validate_nearby_tickets(n_tickets, allowed_ranges):
    sum_n = 0
    valid_t = []
    for t in n_tickets:
        nums = []
        for n in t:
            n_in_r = [n not in r for r in allowed_ranges]
            if all(n_in_r):
                nums.append(n)

        if not nums:
            valid_t.append(t)
        else:
            sum_n += sum(nums)
    return sum_n, valid_t


def match_fields_to_numbers(fields, n_tickets, my_ticket):
    n_tickets.append(my_ticket)
    res = []
    for i in range(len(my_ticket)):
        nums = [t[i] for t in n_tickets]
        k = [k for k, v in fields.items() if all(
            list(map(lambda x: x in v[0] or x in v[1], nums)))]
        res.append(set(k))
    return res


def choose_single_field_for_col(ticket, all_fields):
    res = {}
    visited = set()
    while visited != all_fields:
        for fields, n in ticket:
            if len(fields) == 1:
                chosen = fields.pop()
                visited.add(chosen)
                res[chosen] = n
            else:
                fields -= visited
    return res


if __name__ == "__main__":
    fields, my_ticket, neatby_tickets = read_input('res//16.txt')

    n_tickets = parse_tickets(neatby_tickets)
    my_ticket = parse_tickets(my_ticket)[0]
    fields = parse_fields(fields)

    # Part one
    allowed_ranges = [r for v in fields.values() for r in v]
    sum_nums, valid_t = validate_nearby_tickets(n_tickets, allowed_ranges)
    print(sum_nums)

    # Part two
    possible_fields = match_fields_to_numbers(fields, valid_t, my_ticket)
    sort_by_possible_fields = sorted(
        list(zip(possible_fields, my_ticket)), key=lambda x: len(x[0]))
    ticket = choose_single_field_for_col(sort_by_possible_fields, set(fields))

    print(prod([v for k, v in ticket.items() if k.startswith('departure')]))
