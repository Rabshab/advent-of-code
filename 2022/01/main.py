with open("input") as i:
    input = [int(x) if x != '' else None for x in i.read().splitlines()]

def task1():
    highest_total = 0
    current_total = 0
    for cal in input: 
        if cal == None:
            current_total = 0
            continue
        current_total += cal
        if current_total > highest_total:
            highest_total = current_total

    print(highest_total)

def task2():
    elf_counter = 0
    totals = {} 
    current_total = 0
    for cal in input:
        if cal == None:
            elf_counter +=1
            current_total = 0
            continue
        current_total += cal
        totals[elf_counter] = current_total

    list_of_totals = list(totals.values())
    list_of_totals.sort(reverse=True)
    print(sum(list_of_totals[:3]))



