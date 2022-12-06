import sys

def get_input():
    # Read input from stdin, return a list
    puzzle_input = sys.stdin.read().strip()
    return puzzle_input


def part1(puzzle_input):
    string_list = list(puzzle_input)

    for i, ele in enumerate(string_list):
        group_original = string_list[i : i +4]
        group_set = set(group_original)
        if len(group_original) != len(group_set):
            pass
        else:
            break
    return (i+4)

    

def part2():
    string_list = list(puzzle_input)

    for i, ele in enumerate(string_list):
        group_original = string_list[i : i +14]
        group_set = set(group_original)
        if len(group_original) != len(group_set):
            pass
        else:
            break
    return (i+14)


puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2()))


