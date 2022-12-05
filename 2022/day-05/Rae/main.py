import sys

def get_input():
    # Read input from stdin, return a list
    puzzle_input = sys.stdin.read().strip().split("\n")
    return puzzle_input


def part1(puzzle_input):
    list_1 = ['P','Z','M','T','R','C','N']
    list_2 = ['Z','B','S','T','N','D']
    list_3 = ['G','T','C','F','R','Q','H','M']
    list_4 = ['Z','R','G']
    list_5 = ['H','R','N','Z']
    list_6 = ['D','L','Z','P','W','S','H','F']
    list_7 = ['M','G','C','R','Z','D','W']
    list_8 = ['Q','Z','W','H','L','F','J','S']
    list_9 = ['N','W','P','Q','S']
    list = [list_1, list_2,list_3,list_4,list_5,list_6,list_7,list_8,list_9]
    for i in range (len(puzzle_input)):
        row = puzzle_input[i].split(' ')
        move_number = int(row[1])
        list_from = int(row[3])
        list_to = int(row[5])
        temp = list[list_from-1][:move_number]
        temp.reverse()
        del list[list_from-1][:move_number]
        list[list_to - 1] = temp + list[list_to - 1]  
    final =[]
    for j, ele in enumerate(list):
        final.append(ele[0])
    return (''.join(final))
    

def part2():
    list_1 = ['P','Z','M','T','R','C','N']
    list_2 = ['Z','B','S','T','N','D']
    list_3 = ['G','T','C','F','R','Q','H','M']
    list_4 = ['Z','R','G']
    list_5 = ['H','R','N','Z']
    list_6 = ['D','L','Z','P','W','S','H','F']
    list_7 = ['M','G','C','R','Z','D','W']
    list_8 = ['Q','Z','W','H','L','F','J','S']
    list_9 = ['N','W','P','Q','S']
    list = [list_1, list_2,list_3,list_4,list_5,list_6,list_7,list_8,list_9]
    for i in range (len(puzzle_input)):
        row = puzzle_input[i].split(' ')
        move_number = int(row[1])
        list_from = int(row[3])
        list_to = int(row[5])
        temp = list[list_from-1][:move_number]
        # temp.reverse()
        del list[list_from-1][:move_number]
        list[list_to - 1] = temp + list[list_to - 1]  
    final =[]
    for j, ele in enumerate(list):
        final.append(ele[0])
    return (''.join(final))


puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2()))


