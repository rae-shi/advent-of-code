import sys


def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n")

    # Do extra parsing here if you need
    # eg. puzzle_input = puzzle_input[0].split(" ")

    return puzzle_input


def part1(puzzle_input):
    # x = 0 
    # y = 0

    # for line in puzzle_input:
    #     z = line.split( " ")
    #     if 'forward' in z[0]:
    #         x += int(z[1])
    #     elif 'down' in z[0]:
    #         y += int(z[1])
    #     elif 'up' in z[0]:
    #         y -= int(z[1])
    

    # return x*y
    pass

def part2(puzzle_input):

    def parseDirection(input):
        direction_letter = input[0]
        number = input[1:]
        return (direction_letter, number)

    # central port position
    x = 0 
    y = 0

    # first wire
    line1 = puzzle_input[0].split(",")
    line2 = puzzle_input[1].split(",")


    for token in line1:
        x1 = 0
        y1 = 0
        direction_letter, number = parseDirection(token)
        if direction_letter == 'R':
            x1 += int(number)
        elif direction_letter == 'L':
            x1 -= int(number)
        elif direction_letter == 'U':
            y1 += int(number)
        elif direction_letter == 'D':
            y1 -= int(number)
    
    for token in line2:
        x2 = 0
        y2 = 0
        direction_letter, number = parseDirection(token)
        if direction_letter == 'R':
            x2 += int(number)
        elif direction_letter == 'L':
            x2 -= int(number)
        elif direction_letter == 'U':
            y2 += int(number)
        elif direction_letter == 'D':
            y2 -= int(number)



puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))
