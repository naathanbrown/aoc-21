with open('./day10/input.txt') as f:
    puzzle_input = f.read().splitlines()

class TrackedList:
    def __init__(self):
        self.list = []

    def add_symbol(self, symbol):
        self.list.append(symbol)

    def remove_symbol(self, symbol):
        if symbol == ")":
            inverse_symbol = "("
        elif symbol == "]":
            inverse_symbol = "["
        elif symbol == "}":
            inverse_symbol = "{"
        else:
            inverse_symbol = "<"

        if self.list[-1] == inverse_symbol:
            self.list.pop(-1)
            return None
        else:
            return symbol


close_list = [")", "]", "}", ">"]
score_dict = {")": 3, "]": 57, "}": 1197, ">": 25137}
score = 0
for line in puzzle_input:
    line_list = TrackedList()
    for char in line:
        if char in close_list:
            res = line_list.remove_symbol(char)
            if res != None:
                score += score_dict[res]
                break
        else:
            line_list.add_symbol(char)
    if len(line_list.list) != 0:
        print("incomplete", res)

print(score)