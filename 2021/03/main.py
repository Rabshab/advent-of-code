from collections import Counter

with open("input") as i:
    input = [x for x in i.read().splitlines()]


def task1():
    gamma = ""
    epsilon = ""
    for i in range(len(input[0])):
        c = Counter([x[i] for x in input])
        most_common = c.most_common(2)
        gamma += most_common[0][0]
        epsilon += most_common[1][0]

    print("--------------------")
    print("TASK 1")
    print(gamma)
    print(epsilon)
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    print(gamma)
    print(epsilon)
    print(gamma * epsilon)


def task2():
    co2_input = input
    o2_input = input

    i = 0
    while len(co2_input) > 1 and i < len(co2_input[0]):
        c = Counter([x[i] for x in co2_input])
        most_common = c.most_common(2)
        if most_common[0][1] == most_common[1][1]:
            most_common = [["1"]]
        co2_input = [x for x in co2_input if x[i] == most_common[0][0]]
        i += 1

    i = 0
    while len(o2_input) > 1 and i < len(o2_input[0]):
        c = Counter([x[i] for x in o2_input])
        most_common = c.most_common(2)
        if most_common[0][1] == most_common[1][1]:
            most_common = [[], ["0"]]
        o2_input = [x for x in o2_input if x[i] == most_common[1][0]]
        i += 1

    print("--------------------")
    print("TASK 2")
    print(co2_input)
    print(o2_input)
    print(int(co2_input[0], 2))
    print(int(o2_input[0], 2))
    print(int(co2_input[0], 2) * int(o2_input[0], 2))


task1()
task2()
