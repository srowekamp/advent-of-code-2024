def load(filename='input.txt'):
    rows = list()
    with open(filename) as f:
        for line in f.readlines():
            line = line.strip()
            rows.append(line)
    return rows

def check_pattern_a(rows, x, y):
    count = 0
    # up
    if y > 2:
        # up left
        if x > 2:
            if rows[y-1][x-1] == 'M':
                if rows[y-2][x-2] == 'A':
                    if rows[y-3][x-3] == 'S':
                        count += 1
        # up middle
        if rows[y-1][x] == 'M':
            if rows[y-2][x] == 'A':
                if rows[y-3][x] == 'S':
                    count += 1
        # up right
        if x < len(rows[y])-3:
            if rows[y-1][x+1] == 'M':
                if rows[y-2][x+2] == 'A':
                    if rows[y-3][x+3] == 'S':
                        count += 1
    # right
    if x < len(rows[y]) - 3:
        if rows[y][x+1] == 'M':
            if rows[y][x+2] == 'A':
                if rows[y][x+3] == 'S':
                    count += 1
    # check left
    if x > 2:
        if rows[y][x-1] == 'M':
            if rows[y][x-2] == 'A':
                if rows[y][x-3] == 'S':
                    count += 1
    # check down
    if y < len(rows)-3:
        # down left
        if x > 2:
            if rows[y + 1][x - 1] == 'M':
                if rows[y + 2][x - 2] == 'A':
                    if rows[y + 3][x - 3] == 'S':
                        count += 1
        # down middle
        if rows[y + 1][x] == 'M':
            if rows[y + 2][x] == 'A':
                if rows[y + 3][x] == 'S':
                    count += 1
        # down right
        if x < len(rows[y]) - 3:
            if rows[y + 1][x + 1] == 'M':
                if rows[y + 2][x + 2] == 'A':
                    if rows[y + 3][x + 3] == 'S':
                        count += 1
    return count


def check_a(rows):
    count = 0
    for y,row in enumerate(rows):
        for x,val in enumerate(row):
            if val == 'X':
                matches = check_pattern_a(rows, x, y)
                count += matches
                #print(f'({x},{y}: {matches})')
    return count

def check_b(rows, debug=False):
    count = 0
    for y, row in enumerate(rows):
        for x, val in enumerate(row):
            if val == 'A':
                valid = True
                try:
                    if y == 0 or y == len(rows) - 1:
                        continue
                    if x == 0 or x == len(rows[y]) - 1:
                        continue
                    ul = rows[y-1][x-1]
                    ur = rows[y-1][x+1]
                    bl = rows[y+1][x-1]
                    br = rows[y+1][x+1]

                    if ul == 'S':
                        if br != 'M':
                            continue
                    elif ul == 'M':
                        if br != 'S':
                            continue
                    else:
                        continue
                    if ur == 'S':
                        if bl != 'M':
                            continue
                    elif ur == 'M':
                        if bl != 'S':
                            continue
                    else:
                        continue
                except IndexError:
                    continue
                count += 1
                if debug:
                    print(f'({x},{y})')
                    print(f' {ul} . {ur}\n . A .\n {bl} . {br}')
                    print()
                    input()
    return count

if __name__ == '__main__':
    r = load()
    print(check_a(r))
    print(check_b(r))