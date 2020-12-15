# https://adventofcode.com/2020/day/12

def load_commands(file):
    with open(file) as f:
        commands = [(line.strip()[0], int(line.strip()[1:]))
                    for line in f.readlines()]
    return commands


class Ship:
    def __init__(self):
        self.direction = 'E'
        self.coord = {'EW': 0, 'SN': 0}
        self.__move = {'E': +1, 'S': -1, 'W': -1, 'N': +1}

    def __change_direction(self, d):
        directions = ['N', 'E', 'S', 'W']
        pos = directions.index(self.direction)
        pos += 1 if d == 'R' else - 1

        if pos == -1:
            pos = len(directions) - 1
        elif pos == len(directions):
            pos = 0
        self.direction = directions[pos]

        return directions[pos]

    def get_manhattan_distance(self):
        return abs(self.coord['EW']) + abs(self.coord['SN'])

    def turn(self, d, degrees):
        turns = degrees // 90
        for i in range(turns):
            self.__change_direction(d)

    def move(self, d, units):
        if d == 'F':
            d = self.direction

        if d in 'EW':
            self.coord['EW'] += self.__move[d] * units
        else:
            self.coord['SN'] += self.__move[d] * units
        return self.coord


def parse_instructions(ship: Ship, commands):
    for d, v in commands:
        if d in 'LR':
            ship.turn(d, v)
        else:
            ship.move(d, v)

        #print(ship.coord, ship.waypoint)
    return ship.get_manhattan_distance()


# Different approach for part 2

def rotate(v, r):
    x, y = v
    return [x*r[0][0] + y*r[0][1], x*r[1][0] + y*r[1][1]]


def parse_instructions2(commands):

    # Rotation Matrix
    rotations = {
        "R90": [[0, 1], [-1, 0]],
        "R180": [[-1, 0], [0, -1]],
        "R270": [[0, -1], [1, 0]],
        "L90": [[0, -1], [1, 0]],
        "L180": [[-1, 0], [0, -1]],
        "L270": [[0, 1], [-1, 0]]
    }

    x = y = 0
    v = [10, 1]
    for action, value in commands:
        if action == 'N':
            v[1] += value
        elif action == 'S':
            v[1] -= value
        elif action == 'E':
            v[0] += value
        elif action == 'W':
            v[0] -= value
        elif action in 'LR':
            v = rotate(v, rotations[f"{action}{value}"])
        elif action == 'F':
            x += v[0] * value
            y += v[1] * value
    return abs(x)+abs(y)


if __name__ == "__main__":
    c = load_commands('res\\12.txt')

    # Part 1
    print(parse_instructions(Ship(), c))

    # Part 2
    print(parse_instructions2(c))
