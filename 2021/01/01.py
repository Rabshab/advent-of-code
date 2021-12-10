with open("input") as i:
    input = [int(x) for x in i.read().splitlines()]

count = 0

for i in range(len(input) - 1):
    if input[i + 1] > input[i]:
        count += 1

print(count)

window_length = 3
window_count = 0


def get_window_sum(index):
    return input[index] + input[index + 1] + input[index + 2]


for i in range(len(input) - window_length):
    if get_window_sum(i + 1) > get_window_sum(i):
        window_count += 1

print(window_count)
