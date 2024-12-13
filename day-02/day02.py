from enum import Enum

class Direction(Enum):
    UNKNOWN = 0
    INCREASING = 1
    DECREASING = 2


def safe(test):
    current = test[0]
    direction = Direction.UNKNOWN
    for i in test[1:]:
        # condition 1
        if current < i:
            new_direction = Direction.INCREASING
        elif current > i:
            new_direction = Direction.DECREASING
        else:
            return False
        if direction == Direction.UNKNOWN:
            direction = new_direction
        else:
            if direction != new_direction:
                return False
        # condition 2
        delta = abs(current - i)
        if delta > 3:
            return False
        current = i
    return True

def safe_with_dampener(test):
    if safe(test):
        return True
    for i,v in enumerate(test):
        fixed = test.copy()
        fixed.pop(i)
        if safe(fixed):
            return True
    return False


def load():
    data = []
    with open("input.txt") as f:
        for line in f.readlines():
            line = line.strip()
            data.append(list(map(int, line.split())))
    return data

def obj_a():
    data = load()
    res = list(map(safe, data))
    print(f'there are {res.count(True)} safe tests')

def obj_b():
    data = load()
    res = list(map(safe_with_dampener, data))
    print(f'there are {res.count(True)} safe tests')

if __name__ == '__main__':
    obj_a()
    obj_b()