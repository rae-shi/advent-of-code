import sys

def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n\n")
    return puzzle_input

def part1(puzzle_input):
    elf_list = []
    def calc():
        for i, elf in enumerate(puzzle_input):
            individual_elf = puzzle_input[i].split("\n")
            sum = 0
            for j, food in enumerate(individual_elf):
                sum += int(individual_elf[j])
            elf_list.append(sum)
    calc()
    return (elf_list, max(elf_list))


def swap(list, i, j):
    temp = list[i]
    list[i] = list[j]
    list[j] = temp
    return list

def part2():
    elf_list = part1(puzzle_input)[0]
    length = len(elf_list)
    flag = True
    while flag:
        flag = False
        for i in range(1, length):
            if elf_list[i - 1] < elf_list[i]:
                elf_list = swap(elf_list, i -1, i)
                flag = True
        length -= 1
    sum = 0
    for i, number in enumerate(elf_list[:3]):
        sum += number
    return sum



   


puzzle_input = get_input()
part2()

print("Part 1: {}".format(part1(puzzle_input)[1]))
print("Part 2: {}".format(part2()))


