with open("input") as i:
    input = [x.split(",") for x in i.read().splitlines()]
    number_pairs = [
        [[int(x) for x in pair[0].split("-")], [int(y) for y in pair[1].split("-")]]
        for pair in input
    ]


def contains(one, other):
    if one[0] <= other[0] and one[1] >= other[1]:
        return True
    return False


def overlaps(one, other):
    if (one[0] >= other[0] and one[0] <= other[1]) or (
        one[1] >= other[0] and one[1] <= other[1]
    ):
        return True
    return False


def task1():
    count_fully_contain = 0
    for pair in number_pairs:
        if contains(pair[0], pair[1]) or contains(pair[1], pair[0]):
            count_fully_contain += 1
    print(count_fully_contain)


def task2():
    count_overlap = 0
    for pair in number_pairs:
        if overlaps(pair[0], pair[1]) or overlaps(pair[1], pair[0]):
            count_overlap += 1
    print(count_overlap)

