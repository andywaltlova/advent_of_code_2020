# https://adventofcode.com/2020/day/4


def read_valid_passports(path):
    res = []
    with open(path) as f:
        lines = f.readlines()
        lines.append('\n')

        passport = ''
        for line in lines:
            if line == '\n':
                p = parse_passport(passport)
                if p:
                    res.append(p)
                passport = ''
            passport += line

    return res


def parse_passport(passport):
    p = [f.split(':') for f in passport.replace('\n', ' ').strip().split(' ')]
    p = {k: v for k, v in p}

    # for part one solutions, check_valid_fields is omitted
    if (len(p) >= 8 or (len(p) >= 7 and 'cid' not in p)) and check_valid_fields(p):
        return p


def check_valid_fields(p):
    def hcl_f(x): return x.isdigit() or x in ['a', 'b', 'c', 'd', 'e', 'f']
    k_map = {'byr': lambda x: 1920 <= int(x) <= 2002,
             'iyr': lambda x: 2010 <= int(x) <= 2020,
             'eyr': lambda x: 2010 <= int(x) <= 2030,
             'hgt': lambda x: (x[-2:] == 'cm' and 150 <= int(x[:-2]) <= 193) or (x[-2:] == 'in' and 59 <= int(x[:-2]) <= 76),
             'hcl': lambda x: x[0] == '#' and len(x) == 7 and all(map(hcl_f, x[1:])),
             'ecl': lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
             'pid': lambda x: x.isdigit() and len(x) == 9,
             'cid': lambda x: True}
    return all([k_map[k](v) for k, v in p.items()])


if __name__ == "__main__":
    path = 'res/4.txt'
    print(len(read_valid_passports(path)))
