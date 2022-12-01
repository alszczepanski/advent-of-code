with open("data.txt", "r") as f:
    # PART 1
    calories_goblin = 0
    current = 0
    for line in f:
        if line == "\n":
            if current >= calories_goblin:
                calories_goblin = current
            current = 0
        else:
            current += int(line)

print(calories_goblin)

# PART 2

with open("data.txt", "r") as f:
    list_data = [int(line) if line != "\n" else -1 for line in f]

max_val = 0
sum_list = []
for val in list_data:
    if val != -1:
        max_val += val
    else:
        sum_list.append(max_val)
        max_val = 0

sum_list.sort(reverse=True)


print(sum_list[0] + sum_list[1] + sum_list[2])
