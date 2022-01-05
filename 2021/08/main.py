with open("input") as i:
    lines = [x.split(" | ") for x in i.read().splitlines()]
    inputs = [x[0].split() for x in lines]
    outputs = [x[1].split() for x in lines]


def task1():
    flat_list = [value for values in outputs for value in values]
    uniques = [value for value in flat_list if len(value) in [2, 3, 4, 7]]
    print(uniques)
    print(len(uniques))


def get_bottom_right(values, letters):
    digit_one = next(value for value in values if len(value) == 2)
    len_six_digits = [value for value in values if len(value) == 6]
    for letter in letters:
        six_digits_containing_letter = [
            value for value in len_six_digits if letter in value
        ]
        if letter in digit_one and len(six_digits_containing_letter) == 3:
            return letter


def get_top_right(values, letters):
    digit_one = next(value for value in values if len(value) == 2)
    len_six_digits = [value for value in values if len(value) == 6]
    for letter in letters:
        six_digits_containing_letter = [
            value for value in len_six_digits if letter in value
        ]
        if letter in digit_one and len(six_digits_containing_letter) == 2:
            return letter


def get_middle(values, letters):
    digit_one = next(value for value in values if len(value) == 2)
    digit_four = next(value for value in values if len(value) == 4)
    len_five_digits = [value for value in values if len(value) == 5]
    for letter in letters:
        len_five_digits_containing_letter = [
            value for value in len_five_digits if letter in value
        ]
        if (
            letter in digit_four
            and letter not in digit_one
            and len(len_five_digits_containing_letter) == 3
        ):
            return letter


def is_one(value):
    return len(value) == 2


def is_two(value, top_right, bottom_right):
    return len(value) == 5 and top_right in value and bottom_right not in value


def is_three(value, top_right, bottom_right):
    return len(value) == 5 and top_right in value and bottom_right in value


def is_four(value):
    return len(value) == 4


def is_five(value, top_right, bottom_right):
    return len(value) == 5 and top_right not in value and bottom_right in value


def is_six(value, top_right, bottom_right):
    return len(value) == 6 and top_right not in value and bottom_right in value


def is_seven(value):
    return len(value) == 3


def is_eight(value):
    return len(value) == 7


def is_nine(value, top_right, bottom_right, middle):
    return (
        len(value) == 6
        and top_right in value
        and bottom_right in value
        and middle in value
    )


def is_zero(value, top_right, bottom_right, middle):
    return (
        len(value) == 6
        and top_right in value
        and bottom_right in value
        and middle not in value
    )


def get_digit(value, top_right, bottom_right, middle):
    if is_one(value) == True:
        return "1"
    if is_two(value, top_right, bottom_right) == True:
        return "2"
    if is_three(value, top_right, bottom_right) == True:
        return "3"
    if is_four(value) == True:
        return "4"
    if is_five(value, top_right, bottom_right) == True:
        return "5"
    if is_six(value, top_right, bottom_right) == True:
        return "6"
    if is_seven(value) == True:
        return "7"
    if is_eight(value) == True:
        return "8"
    if is_nine(value, top_right, bottom_right, middle) == True:
        return "9"
    if is_zero(value, top_right, bottom_right, middle) == True:
        return "0"


def task2():
    letters = ["a", "b", "c", "d", "e", "f", "g"]
    solved_outputs = []
    for i in range(len(inputs)):
        top_right = get_top_right(inputs[i], letters)
        bottom_right = get_bottom_right(inputs[i], letters)
        middle = get_middle(inputs[i], letters)
        output_digits = []
        for output in outputs[i]:
            output_digits.append(get_digit(output, top_right, bottom_right, middle))
        solved_outputs.append(int("".join(output_digits)))

    print(sum(solved_outputs))
