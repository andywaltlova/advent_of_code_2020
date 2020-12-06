# https://adventofcode.com/2020/day/5


def read_input(path):
    with open(path) as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def decode_seat_id(b_pass):
    rows = reduce_range(b_pass[:7], range(128), 'F', 'B')
    cols = reduce_range(b_pass[7:], range(8), 'L', 'R')
    return rows * 8 + cols


def reduce_range(string, interval, lower, upper):
    for c in string:
        middle = len(interval) // 2
        interval = interval[:middle] if c == lower else interval[middle:]
    return interval[0]


def find_seat(seats):
    for i in range(len(seats) - 2):
        if seats[i + 1] - seats[i] > 1:
            return seats[i] + 1


if __name__ == "__main__":
    b_passes = read_input('res/5.txt')

    test_passes = ['FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']
    t_nums = [decode_seat_id(t) for t in test_passes]
    assert t_nums == [357, 567, 119, 820]

    # Part-one
    seat_ids = [decode_seat_id(b) for b in b_passes]
    print(max(seat_ids))

    # Part-two
    my_seat = find_seat(sorted(seat_ids))
    print(my_seat)
