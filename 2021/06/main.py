import math

with open("input") as i:
    fish = [int(x) for x in i.read().split(",")]


def task1():
    number_of_days = 0
    new_fish = []
    while number_of_days < 80:
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] < 0:
                fish[i] = 6
                new_fish.append(8)
        fish.extend(new_fish)
        new_fish = []
        number_of_days += 1

    print(len(fish))


# Hint taken to use counts instead of length after failed attempts to model number of children.
def task2():
    counts = [fish.count(i) for i in range(9)]
    for i in range(256):
        number_giving_birth = counts.pop(0)
        counts[6] += number_giving_birth
        counts.append(number_giving_birth)
    print(sum(counts))


task1()
task2()
