import re


def obj_a():
    reg = re.compile(r'mul\((\d+),(\d+)\)')
    sum = 0
    with open("input.txt") as f:
        for line in f.readlines():
            matches = reg.findall(line)
            for match in matches:
                a,b = match
                sum += int(a) * int(b)
    print(sum)

def obj_b():
    reg = re.compile(r'(do\(\))|(don\'t\(\))|mul\((\d+),(\d+)\)')
    sum = 0
    enabled = True
    with open("input.txt") as f:
        for line in f.readlines():
            matches = reg.findall(line)
            for match in matches:
                do, don, a, b = match
                if do != '':
                    enabled = True
                    continue
                elif don != '':
                    enabled = False
                    continue
                elif enabled:
                    sum += int(a) * int(b)
    print(sum)

if __name__ == "__main__":
    obj_a()
    obj_b()
