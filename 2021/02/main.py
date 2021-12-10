def split_command(input_line):
    split = input_line.split()
    return [split[0], int(split[1])]


with open("input") as i:
    input = [split_command(x) for x in i.read().splitlines()]

position = {"horizontal": 0, "aim": 0, "depth": 0}

for i in range(len(input)):
    if input[i][0] == "forward":
        position["horizontal"] += input[i][1]
        position["depth"] += input[i][1] * position["aim"]
    if input[i][0] == "down":
        position["aim"] += input[i][1]
    if input[i][0] == "up":
        position["aim"] -= input[i][1]

print(position)
print(position["horizontal"] * position["depth"])
