import sys

def get_input():
    # Read input from stdin
    puzzle_input = sys.stdin.read().strip().split("\n")
    return puzzle_input

def part1(puzzle_input):
    total_score = 0
    for i, ele in enumerate(puzzle_input):
        # play = puzzle_input.split(" ")
        elf_play = puzzle_input[i][0]
        user_play = puzzle_input[i][2]
        def rpc():
            sum = 0
            # user plays rock
            if user_play =="X":
                score_plus = 1
                # elf plays rock
                if elf_play == "A":
                    round_score = score_plus + 3
                    sum += round_score
                # elf plays paper
                elif elf_play == "B":
                    round_score = score_plus + 0
                    sum += round_score
                # elf plays scissor
                else:
                    round_score = score_plus + 6
                    sum += round_score
            # user plays paper
            elif user_play =="Y":
                score_plus = 2
                # elf plays paper
                if elf_play == "B":
                    round_score = score_plus + 3
                    sum += round_score
                # elf plays scissor
                elif elf_play == "C":
                    round_score = score_plus + 0
                    sum += round_score
                # elf plays rock
                else:
                    round_score = score_plus + 6
                    sum += round_score
             # user plays scissor
            else:
                score_plus = 3
                # elf plays scissor
                if elf_play == "C":
                    round_score = score_plus + 3
                    sum += round_score
                # elf plays rock
                elif elf_play == "A":
                    round_score = score_plus + 0
                    sum += round_score
                # elf plays paper
                else:
                    round_score = score_plus + 6
                    sum += round_score          
            return sum
        sum = rpc()
        total_score += sum
    return total_score


def part2():
    total_score = 0
    for i, ele in enumerate(puzzle_input):
        # play = puzzle_input.split(" ")
        elf_play = puzzle_input[i][0]
        user_play = puzzle_input[i][2]
        def rpc():
            sum = 0
            # user needs to lose
            if user_play =="X":
                score = 0
                # elf plays rock, user plays scissor
                if elf_play == "A":
                    round_score = score + 3
                    sum += round_score
                # elf plays paper, user plays rock
                elif elf_play == "B":
                    round_score = score + 1
                    sum += round_score
                # elf plays scissor, user plays paper
                else:
                    round_score = score + 2
                    sum += round_score
            # user needs to draw
            elif user_play =="Y":
                score = 3
                # elf plays paper, user plays paper
                if elf_play == "B":
                    round_score = score + 2
                    sum += round_score
                # elf plays scissor, user plays scissor
                elif elf_play == "C":
                    round_score = score + 3
                    sum += round_score
                # elf plays rock, user plays rock
                else:
                    round_score = score + 1
                    sum += round_score
             # user needs to win
            else:
                score = 6
                # elf plays scissor, user plays rock 
                if elf_play == "C":
                    round_score = score + 1
                    sum += round_score
                # elf plays rock, user plays paper
                elif elf_play == "A":
                    round_score = score + 2
                    sum += round_score
                # elf plays paper, user plays scissor
                else:
                    round_score = score + 3
                    sum += round_score          
            return sum
        sum = rpc()
        total_score += sum
    return total_score

puzzle_input = get_input()

print("Part 1: {}".format(part1(puzzle_input)))
print("Part 2: {}".format(part2()))


