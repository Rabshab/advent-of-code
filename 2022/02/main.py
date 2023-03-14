with open("input") as i:
    input = [x.split(" ") for x in i.read().splitlines()]

same = {"A": "X", "B": "Y", "C": "Z"}
beats = {"A": "Z", "B": "X", "C": "Y"}
score = {"X": 1, "Y": 2, "Z": 3}


def task1():
    points = 0
    for round in input:
        if beats[round[0]] == round[1]:
            points += score[round[1]]
        elif same[round[0]] == round[1]:
            points += 3
            points += score[round[1]]
        else:
            points += 6
            points += score[round[1]]
    print(points)


same = {"A": 1, "B": 2, "C": 3}
beats = {"A": 3, "B": 1, "C": 2}
loses = {"A": 2, "B": 3, "C": 1}


def task2():
    points = 0
    for round in input:
        if round[1] == "X":
            points += beats[round[0]]
        elif round[1] == "Y":
            points += 3
            points += same[round[0]]
        else:
            points += 6
            points += loses[round[0]]
    print(points)


task2()
