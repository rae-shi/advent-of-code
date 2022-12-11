import sys

def get_input():
    # Read input from stdin, return a list
    puzzle_input = sys.stdin.read().strip().split("\n")
    return puzzle_input


def part1(puzzle_input):
    dic = {}
    cycle = 0
    value = 1
    for i in range (len(puzzle_input)):
        row = puzzle_input[i].split(' ')
        instruction = row[0]
        if instruction == 'addx':
            movement = int(row[1])
        else:
            movement = 0
        if instruction == 'noop':
            cycle += 1
            value += 0
            dic[cycle] = value
        else:
            for j in range(0, 2):
                cycle += 1
                if j == 1:
                    dic[cycle] = value
                    value += movement
                else:
                    value += 0
                    dic[cycle] = value
    sum = dic[20] * 20 + dic[60] * 60 + dic[100] * 100 + dic[140] * 140 + dic[180] * 180 + dic[220] * 220
    return (dic, sum)

    

def part2():
    dic = part1(puzzle_input)[0]
    print(dic)
    row_number = ((len(dic)-1) // 40) + 1
    total_list =[]
    for j in range(0, row_number):
        row = '.'
        added_ele = '.'
        for i in range(0,39):
            row = ''.join([row, added_ele])
        row_list = list(row)
        total_list.append(row_list)
    print(total_list)
    for m in range(0, len(total_list)):
        for n in range(1, 41):
            multi = m 
            x = dic[n + multi * 40]
            spirit_position = [ str(x), str(x + 1),str(x + 2)]
            if str(n) in spirit_position:
                total_list[m][n-1] ='#'          
    for m in range(0, len(total_list)):
        tempt = total_list[m]
        joined_str = ' '.join(tempt)
        print(joined_str)
        
puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2()))


