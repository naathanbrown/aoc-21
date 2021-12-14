with open('./day11/input.txt') as f:
    puzzle_input = f.read().splitlines()

class OctoBoard():
    def __init__(self, input):
        self.board = []
        for line in input:
            line_len = len(line)
            self.board.append([-2] + list(map(int,line)) + [-2])
        self.board = [[-2] * (line_len + 2)] + self.board
        self.board.append([-2] * (line_len + 2))

        self.score = 0

    def ToString(self):
        for idx, line in enumerate(self.board):
            if idx == 0 or idx == len(self.board) - 1:
                test = 1
            else:
                print(line[1:-1])
    
    def increase_all(self):
        for idx, line in enumerate(self.board):
            self.board[idx] = [x+1 if x != -2 else x for x in line ]

    def bust_the_nines(self):
        for idx, line in enumerate(self.board):
            for idy, number in enumerate(line):
                if number >= 10:
                    self.flash(idx, idy)

    def flash(self, idx, idy):
        self.score += 1
        self.board[idx][idy] = -1
        for i in range(-1, 2):
            for j in range(-1, 2):
                if self.board[idx + i][idy + j] != -2 and not (i == 0 and j == 0):
                    if self.board[idx + i][idy + j] != -1:
                        self.board[idx + i][idy + j] += 1
                    if self.board[idx + i][idy + j] >= 10:
                        self.flash(idx + i, idy + j)

    def clean_board(self):
        for idx, line in enumerate(self.board):
            for idy, number in enumerate(line):
                if number == -1:
                    self.board[idx][idy] = 0
    

boardObj = OctoBoard(puzzle_input)
print(boardObj.ToString())
for i in range(0,100):
    boardObj.increase_all()
    score = boardObj.bust_the_nines()
    boardObj.clean_board()
    print(boardObj.ToString())

print(boardObj.score)