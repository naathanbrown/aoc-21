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

def inverse_symbol(symbol):
    if symbol == "(":
        inverse_symbol = ")"
    elif symbol == "[":
        inverse_symbol = "]"
    elif symbol == "{":
        inverse_symbol = "}"
    else:
        inverse_symbol = ">"
    
    return inverse_symbol

def check(line):
    line_list = TrackedList()
    for char in line:
        if char in close_list:
            res = line_list.remove_symbol(char)
            if res != None:
                return
        else:
            line_list.add_symbol(char)
    if len(line_list.list) != 0:
        end_list = []
        for char in reversed(line_list.list):
            end_list.append(inverse_symbol(char))
    return end_list

def score_calc(closer):
    score = 0
    for symbol in closer:
        score *= 5
        score += score_dict[symbol]
    return score



close_list = [")", "]", "}", ">"]
score_dict = {")": 1, "]": 2, "}": 3, ">": 4}
score_list = []
for line in puzzle_input:
    res = check(line)
    if res != None:
        score_list.append(score_calc(res))

middleIndex = int((len(score_list) - 1)/2)
print(sorted(score_list, reverse=True)[middleIndex])