
with open("data.txt", "r") as f:
    score = 0
    for line in f:
        line = line.strip()
        range1, range2 = line.split(',')
        val1, val2 = range1.split("-")
        val3, val4 = range2.split("-")
        x = range(int(val1), int(val2)+1)
        y = range(int(val3), int(val4)+1)

        xs = set(x)
        ys = set(y)
        if xs.intersection(y) or ys.intersection(x):
            score += 1

print(score)
