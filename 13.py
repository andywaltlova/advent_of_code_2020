# https://adventofcode.com/2020/day/13

def read_input(path: str):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]

    timestamp = int(lines[0])
    return timestamp, lines[1].split(',')


def find_first_greater_multiple(k, m):
    n = 0
    while n < k:
        n += m
    diff = n - k

    return m, n, diff


def find_bus(timestamp, buses):
    res = [find_first_greater_multiple(timestamp, bus) for bus in buses]
    res = sorted(res, key=lambda bus: bus[1])
    return res[0][0]*res[0][2]


# Part 2
def part_two(buses):
    t, step = 0, buses[0]
    for i, b in filter(lambda x: x[1], enumerate(buses[1:], start=1)):
        while (t + i) % b != 0:
            t += step
        step *= b
    return t


if __name__ == "__main__":
    timestamp, buses = read_input('res\\13.txt')
    buses_without_x = list(map(int, filter(lambda x: x != 'x', buses)))
    # Part 1
    print(find_bus(timestamp, buses_without_x))

    # Part 2
    # replace 'x' to 0
    buses = list(map(int, [b if b != 'x' else 0 for b in buses]))
    print(part_two(buses))
