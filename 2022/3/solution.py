from itertools import islice
import string

lowercase = dict(zip(string.ascii_lowercase, range(1, 27)))
uppercase = dict(zip(string.ascii_uppercase, range(27, 53)))

letters = dict(lowercase)
letters.update(uppercase)

score1 = 0
score2 = 0
# with open("data.txt", "r") as f:
#     for line in f:
#         line = line.strip()
#         first_compartment = line[0:int(len(line)/2)]
#         second_compartment = line[int(len(line)/2):]
#         s = (set(first_compartment).intersection(second_compartment))
#         converted = dict.fromkeys(s, 0)
#         key, value = list(converted.items())[0]
#         # print(key)
#         score1 += letters.get(key)

with open("data.txt", "r") as f:
    while True:
        three_lines = list(islice(f, 3))
        if not three_lines:
            break

        first_group_compartment = ''
        second_group_compartment = ''

        s = set(three_lines[0].strip()) & set(
            three_lines[1].strip()) & set(three_lines[2].strip())

        # s = (set(first_group_compartment).intersection(second_group_compartment))
        print(s)
        converted = dict.fromkeys(s, 0)
        key, value = list(converted.items())[0]

        score2 += letters.get(key)


print(score2)
