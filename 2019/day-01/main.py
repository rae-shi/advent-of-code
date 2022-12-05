import sys
from math import sqrt

#create function to calculate Manhattan distance 
    

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

    def manhattan(a, b):
        return sum(abs(val1-val2) for val1, val2 in zip(a,b))

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
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0

    position_set = set()
    list_intersection = []
    position_dictionary_2 = {}


    for token in line1:   
        direction_letter, number = parseDirection(token)
        for i in range(0, int(number)):
            if direction_letter == 'R':
                x1 += 1
            elif direction_letter == 'L':
                x1 -= 1
            elif direction_letter == 'U':
                y1 -= 1
            elif direction_letter == 'D':
                y1 += 1
            position_set.add((x1,y1))
    # print(position_set)
        
    for token in line2:   
        direction_letter, number = parseDirection(token)
        for i in range(0, int(number)):
            if direction_letter == 'R':
                x2 += 1
            elif direction_letter == 'L':
                x2 -= 1
            elif direction_letter == 'U':
                y2 -= 1
            elif direction_letter == 'D':
                y2 += 1
            if (x2,y2) in position_set:
                list_intersection.append((x2,y2))
    
    print(list_intersection[0][0])

    manhattan_list = []
    for i, intersection in enumerate(list_intersection):
        a=list_intersection[i][0]
        b=list_intersection[i][1]
        A = (a,b )
        B = (0, 0)
        c = manhattan(A, B)
        manhattan_list.append(c)
    print(min(manhattan_list))

        # position_dictionary_2[token]= (x2,y2)
    
    
    
   

    #calculate Manhattan distance between vectors
   
    # print(position_dictionary_2)

    # print(list_intersection)
    



    
puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2(puzzle_input)))
