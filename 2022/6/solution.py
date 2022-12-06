from collections import deque


def find_packet(datastream: str, marker_size: int):
    current_signal = deque([])

    for _, char in enumerate(datastream):
        if _ > marker_size:
            if (check_if_marker(current_signal)):
                return _
            else:
                current_signal.rotate(-1)
                current_signal.pop()
                current_signal.append(char)
        else:
            current_signal.append(char)


def check_if_marker(potential_marker: str):
    potential_marker = sorted(potential_marker)
    for _ in range(len(potential_marker)-1):
        if (potential_marker[_] == potential_marker[_+1]):
            return False
    return True


with open('data.txt', 'r') as f:
    line = f.readline()

print(find_packet(line, 13))
