with open("input") as i:
    input = i.read().splitlines()
    numbers = [int(x) for x in input[0].split(",")]
    board_inputs = input[2:]
    board = 0
    line_count = 0
    boards = []
    for i in range(len(board_inputs)):
        line = [(int(x), 0) for x in board_inputs[i].split(" ") if len(x) > 0]
        if line_count == 0:
            boards.append([])
        if line_count != 5:
            boards[board].append(line)
        line_count += 1
        if line_count == 6:
            line_count = 0
            board += 1


def check_win(board):
    for i in board:
        if all(flag == 1 for (_, flag) in i):
            return i

    for j in list(zip(*board)):
        if all(flag == 1 for (_, flag) in j):
            return j

    return None


def is_stamped(board_tuple, number):
    if board_tuple[0] == number:
        return (board_tuple[0], 1)

    return board_tuple


def update_board(board, number):
    return [[is_stamped(board_tuple, number) for board_tuple in row] for row in board]


def task1():
    used_numbers = []
    has_won = False
    for i in range(len(numbers)):
        if has_won == True:
            break
        number = numbers[i]
        used_numbers.append(number)
        for i in range(len(boards)):
            boards[i] = update_board(boards[i], number)
            win = check_win(boards[i])
            if win is not None:
                inner_sum = [
                    sum(dig for dig, stamp in row if stamp != 1) for row in boards[i]
                ]
                unmarked_sum = sum(inner_sum)
                print(unmarked_sum * number)
                has_won = True


def task2():
    completed_board_indexes = []
    used_numbers = []
    for i in range(len(numbers)):
        number = numbers[i]
        used_numbers.append(number)
        for i in range(len(boards)):
            if not any(index == i for index, number in completed_board_indexes):
                boards[i] = update_board(boards[i], number)
            win = check_win(boards[i])
            if win is not None:
                if not any(index == i for index, number in completed_board_indexes):
                    completed_board_indexes.append((i, number))

    unmarked_row_sums = [
        sum(dig for dig, stamp in row if stamp != 1)
        for row in boards[completed_board_indexes[-1][0]]
    ]
    unmarked_total_sum = sum(unmarked_row_sums)
    print(unmarked_total_sum * completed_board_indexes[-1][1])


# These implementations modify the boards list
# so both tasks cannot be run in sequence
# uncomment function calls as required
# task1()
# task2()
