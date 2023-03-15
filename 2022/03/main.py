with open("input") as i:
    # input = [[x[:len(x)//2], x[len(x)//2:]] for x in i.read().splitlines()]
    input = [list(dict.fromkeys(list(x))) for x in i.read().splitlines()]


def get_priority(item):
    if item.isupper():
        return ord(item) - 38
    return ord(item) - 96


def task1():
    total_priority = 0
    for pair in input:
        for item in list(dict.fromkeys(list(pair[0]))):
            for other_item in list(dict.fromkeys(list(pair[1]))):
                if item == other_item:
                    total_priority += get_priority(item)
                    continue
    print(total_priority)


def is_present_in_list(item, list):
    for other_item in list:
        if item == other_item:
            return True
    return False


def task2():
    total_priority = 0
    i = 0
    while i < len(input) - 2:
        for item in input[i]:
            if is_present_in_list(item, input[i + 1]) and is_present_in_list(
                item, input[i + 2]
            ):
                total_priority += get_priority(item)
                continue
        i += 3
    print(total_priority)

