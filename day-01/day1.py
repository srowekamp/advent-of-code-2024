def load():
    list1 = []
    list2 = []
    with open('input.txt') as f:
        for line in f:
            parts = line.split()
            list1.append(int(parts[0].strip()))
            list2.append(int(parts[1].strip()))
    list1.sort()
    list2.sort()
    return list1, list2
def obj_a():
    list1, list2 = load()

    distances = []

    while len(list1) > 0:
        d1 = list1.pop(0)
        d2 = list2.pop(0)
        distance = abs(d1-d2)
        distances.append(distance)

    print(sum(distances))

def obj_b():
    list1, list2 = load()
    occurrences = dict()
    score = 0
    for i in list1:
        if i not in occurrences:
            count = 0
            for x in list2:
                if x == i:
                    count += 1
            occurrences[i] = count
        else:
            count = occurrences[i]
        score += i * count
    print(score)
if __name__ == "__main__":
    obj_a()
    obj_b()