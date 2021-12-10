def parse_input_line(line_string):
    arrow_removed = line_string.split(" -> ")
    pairs = [
        tuple(int(element) for element in pair.split(",")) for pair in arrow_removed
    ]
    sorted_x = sorted(pairs, key=lambda coord: coord[0])
    return sorted(sorted_x, key=lambda coord: coord[1])


with open("input") as i:
    all = [parse_input_line(x) for x in i.read().splitlines()]
    horiz_and_vert = [x for x in all if x[0][0] == x[1][0] or x[0][1] == x[1][1]]
    horiz = [x for x in all if x[0][1] == x[1][1]]
    vert = [x for x in all if x[0][0] == x[1][0]]


def get_outer_limits(input_list):
    limits = [0, 0]
    for pair in input_list:
        if pair[0][0] > limits[0]:
            limits[0] = pair[0][0]
        if pair[1][0] > limits[0]:
            limits[0] = pair[1][0]
        if pair[0][1] > limits[1]:
            limits[1] = pair[0][1]
        if pair[1][1] > limits[1]:
            limits[1] = pair[1][1]
    return limits


def is_horizontal(pair):
    return pair[0][1] == pair[1][1]


def is_vertical(pair):
    return pair[0][0] == pair[1][0]


def is_down_left(pair):
    return pair[0][0] > pair[1][0] and pair[0][1] < pair[1][1]


def is_down_right(pair):
    return pair[0][0] < pair[1][0] and pair[0][1] < pair[1][1]


def task1():
    limits = get_outer_limits(horiz_and_vert)
    output_matrix = [
        [0 for col in range(limits[0] + 1)] for row in range(limits[1] + 1)
    ]
    for i in horiz:
        for j in range(i[0][0], i[1][0] + 1):
            output_matrix[i[0][1]][j] += 1
    for i in vert:
        for j in range(i[0][1], i[1][1] + 1):
            output_matrix[j][i[0][0]] += 1

    print(output_matrix)
    row_sums = sum([len([x for x in row if x > 1]) for row in output_matrix])
    print(row_sums)


def task2():
    print(all)
    limits = get_outer_limits(all)
    output_matrix = [
        [0 for col in range(limits[0] + 1)] for row in range(limits[1] + 1)
    ]
    for i in all:
        if is_horizontal(i):
            for j in range(i[0][0], i[1][0] + 1):
                output_matrix[i[0][1]][j] += 1
        if is_vertical(i):
            for j in range(i[0][1], i[1][1] + 1):
                output_matrix[j][i[0][0]] += 1
        if is_down_right(i):
            for j in range(0, i[1][1] + 1 - i[0][1]):
                output_matrix[i[0][1] + j][i[0][0] + j] += 1
        if is_down_left(i):
            for j in range(0, i[1][1] + 1 - i[0][1]):
                output_matrix[i[0][1] + j][i[0][0] - j] += 1

    print(output_matrix)
    row_sums = sum([len([x for x in row if x > 1]) for row in output_matrix])
    print(row_sums)


task1()
task2()
