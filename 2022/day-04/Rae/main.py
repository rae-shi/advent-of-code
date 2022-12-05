import sys

def get_input():
    # Read input from stdin, return a list
    puzzle_input = sys.stdin.read().strip().split("\n")
    return puzzle_input


def part1(puzzle_input):
    count = 0
    for i in range (len(puzzle_input)):
        # print(puzzle_input)
        pair = puzzle_input[i].split(',')
        element = []
        for j in range(len(pair)):
            a = pair[j].split('-')
            element = element + a
        if ((int(element[0]) <=int(element[2])) and (int(element[1]))>=int(element[3])):
            count +=1
        elif ((int(element[0]) >=int(element[2])) and (int(element[1])<=int(element[3]))):
            count +=1
    return count

def part2():
    count = 0
    for i in range (len(puzzle_input)):
        pair = puzzle_input[i].split(',')
        element = []
        for j in range(len(pair)):
            a = pair[j].split('-')
            element = element + a
        list_1 = list(range(int(element[0]), int(element[1]) +1))
        list_2 = list(range(int(element[2]), int(element[3]) +1))
        for k, ele in enumerate(list_1):
            if ele in list_2:
                count +=1
                break
    return count


puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2()))


