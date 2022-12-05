import sys

def get_input():
    # Read input from stdin, return a list
    puzzle_input = sys.stdin.read().strip().split("\n")
    return puzzle_input


def part1(puzzle_input):
    same_stuff =[]
    sum = 0
    for i, ele in enumerate(puzzle_input):
        compartment_1 =  ele[:int((len(ele) / 2))]
        compartment_2 =  ele[int((len(ele) / 2)):]
        compartment_1_lis = list(compartment_1)
        compartment_2_lis = list(compartment_2)
        compartment_1_list = set(compartment_1_lis)
        compartment_2_list = set(compartment_2_lis)
        for a, el in enumerate(compartment_1_list):
            if el in compartment_2_list:
                same_stuff.append(el)
    for i, elem in enumerate(same_stuff):
        if elem.islower():
            sum += (int(ord(elem)) - 96)
        else:
            sum += (int(ord(elem)) - 38)
    return sum


def part2():
    same_stuff =[]
    sum = 0
    for i in range(0,len(puzzle_input),3):
        elf_1 =  puzzle_input[i]
        elf_2 =  puzzle_input[i + 1]
        elf_3 =  puzzle_input[i + 2]
        elf_1_list = set(list(elf_1))
        elf_2_list = set(list(elf_2))
        elf_3_list = set(list(elf_3))
        for a, el in enumerate(elf_1_list):
            if (el in elf_2_list) and (el in elf_3_list):
                same_stuff.append(el)
    for i, elem in enumerate(same_stuff):
        if elem.islower():
            sum += (int(ord(elem)) - 96)
        else:
            sum += (int(ord(elem)) - 38)
    return sum

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2()))


