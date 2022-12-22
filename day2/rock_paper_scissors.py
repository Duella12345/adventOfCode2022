# This strategy guide predicts and recommends the following:

# In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
# In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
# The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
# In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).

# What would your total score be if everything goes exactly according to your strategy guide? *
def rock_paper_scissors(filename):
    match_list = open(filename, 'r')
    content = match_list.readlines()
    match_score = 0

    for line in content:
        if "X" in line:
            match_score += 1
            line = line.replace("X", "A")
            if line[0] == 'C':
                match_score += 6
        elif "Y" in line:
            match_score += 2
            line = line.replace("Y", "B")
            if line[0] == 'A':
                match_score += 6
        else:
            match_score += 3
            line = line.replace("Z", "C")
            if line[0] == 'B':
                match_score += 6

        if line[0] == line[2]:
            match_score += 3

    return match_score

print(rock_paper_scissors("day2/rock_paper_scissors_test.txt"))
print(rock_paper_scissors("day2/rock_paper_scissor_input.txt"))

# The Elf finishes helping with the tent and sneaks back over to you. "Anyway, the second column says how the round needs to end: X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win. Good luck!"

# The total score is still calculated in the same way, but now you need to figure out what shape to choose so the round ends as indicated. The example above now goes like this:

# In the first round, your opponent will choose Rock (A), and you need the round to end in a draw (Y), so you also choose Rock. This gives you a score of 1 + 3 = 4.
# In the second round, your opponent will choose Paper (B), and you choose Rock so you lose (X) with a score of 1 + 0 = 1.
# In the third round, you will defeat your opponent's Scissors with Rock for a score of 1 + 6 = 7.
# Now that you're correctly decrypting the ultra top secret strategy guide, you would get a total score of 12. *
def rock_paper_scissors2(filename):
    match_list = open(filename, 'r')
    content = match_list.readlines()
    match_score = 0

    for line in content:
        if "X" in line:
            match_score += 0
            if line[0] == 'A':
                match_score += 3
            elif line[0] == 'B':
                match_score += 1
            elif line[0] == 'C':
                match_score += 2

        elif "Y" in line:
            match_score += 3
            if line[0] == 'A':
                match_score += 1
            elif line[0] == 'B':
                match_score += 2
            elif line[0] == 'C':
                match_score += 3
        else:
            match_score += 6
            if line[0] == 'A':
                match_score += 2
            elif line[0] == 'B':
                match_score += 3
            elif line[0] == 'C':
                match_score += 1

    return match_score

print(rock_paper_scissors2("day2/rock_paper_scissors_test.txt")) # 12
print(rock_paper_scissors2("day2/rock_paper_scissor_input.txt")) # 12881