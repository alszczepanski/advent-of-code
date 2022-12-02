
# A rock
# B paper
# C scissors
# X rock
# Y paper
# Z scissors

# POINTS
# 1 paper
# 2 rock
# 3 scissors
# 6 win
# 3 draw
# 0 lost

results_dict = {
    # draw combinations
    "A X": 4,
    "B Y": 5,
    "C Z": 6,
    # winning combinations
    "A Y": 8,
    "B Z": 9,
    "C X": 7,
    # loosing combinations
    "A Z": 3,
    "B X": 1,
    "C Y": 2
}

modified_dict = {
    # draw combinations
    "A Y": 4,
    "B Y": 5,
    "C Y": 6,
    # winning combinations
    "A Z": 8,
    "B Z": 9,
    "C Z": 7,
    # loosing combinations
    "A X": 3,
    "B X": 1,
    "C X": 2
}
score = 0
with open("data.txt", "r") as f:
    for line in f:
        line = line.strip()
        score += modified_dict.get(line)


print(score)
