import re


class Node:
    def __init__(self):
        self.value = None
        self.next = None

    @classmethod
    def _with_value(cls, value: int):
        v = cls()
        v.value = value
        return v


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    @classmethod
    def _with_size(cls, size: int):
        return cls(size=size)

    def pop(self):
        if not self.empty():
            if self.head.next is not None:
                next_node = Node()
                next_node = self.head.next
                val = self.head.value
                self.head = next_node
                return val
            else:
                val = self.head.value
                self.head = None
                return val
        else:
            return 'empty'

    def push(self, value: int):
        if self.head is None:
            new_node = Node._with_value(value)
            self.head = new_node
            self.head.next = None
        else:
            new_node = Node._with_value(value)
            new_node.next = self.head
            self.head = new_node

    def empty(self):
        if self.head is not None:
            return False
        else:
            return True

    def peek(self):
        if not self.empty():
            return self.head.value
        else:
            return 'empty'


line = []
with open('data.txt', 'r') as f:
    lines = f.readlines()

    for i in range(0, 9):
        lines[i] = lines[i].replace("[", " ")
        lines[i] = lines[i].replace("]", " ")
        line.append(lines[i])

reversed_matrix = []

for row in range(0, 36):
    cols = []
    for col in range(0, 8):
        if line[col][row] != " " and line[col][row] != "\n":
            cols.append(line[col][row])
    if len(cols) > 0:
        cols.reverse()
        reversed_matrix.append(cols)


stackList = [Stack() for _ in range(len(reversed_matrix))]

for _, stack_feed in enumerate(reversed_matrix):
    for val in stack_feed:
        stackList[_].push(val)


def move(qty_of_elements: int, curr_stack_id: int, target_stack_id: int):
    popped = []
    for _ in range(qty_of_elements):
        val = stackList[curr_stack_id].pop()
        popped.append(val)
    popped.reverse()
    for _ in range(qty_of_elements):
        stackList[target_stack_id].push(popped[_])


with open('data.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        if line.startswith('move'):
            vals = re.findall(r'\d+', line)
            print(vals)
            move(int(vals[0]), int(vals[1])-1, int(vals[2])-1)


for _, stack in enumerate(stackList):
    print(stack.peek())
