class BingoBoard:
    def __init__(self, input):
        self.board = [[],[],[],[],[]]
        for i in range(0, 5):
            self.board[i] = list(map(int,list(filter(None, input[i].split(' ')))))

    def SumBoard(self, number):
        score = 0
        for row in self.board:
            row = [0 if x == -1 else x for x in row]
            score += sum(row)
        return score * number

    def CheckBoardAndRemove(self, number):
        for idx, row in enumerate(self.board):
            row = [-1 if x == number else x for x in row]
            self.board[idx] = row
        return self.SumBoard(number) if self.CheckWinner() else self

    def GetColumnNumber(self, row):
        return self.board.index(row)

    def CheckColumnWin(self):
        for row in self.board:
            if -1 in row and self.GetColumnNumber(row) == 0:
                index_list = []
                for idx, value in enumerate(row):
                    if value == -1:
                        index_list.append(idx)
                for idx in index_list:
                    if self.board[1][idx] == -1 and self.board[2][idx] == -1 and self.board[3][idx] == -1 and self.board[4][idx] == -1:
                        return True
        return False

    def CheckRowWin(self):
        for row in self.board:
            if all([ v == -1 for v in row ]):
                return True
        return False
                
    def CheckWinner(self):
        if self.CheckRowWin():
            return True
        elif self.CheckColumnWin():
            return True
        else:
            return False

def game_loop():
    with open('input.txt') as f:
        bingo_input = f.read().splitlines()

    bingo_numbers = list(map(int, bingo_input[0].split(',')))

    bingo_input.pop(0)
    bingo_boards = []

    for idx, input in enumerate(bingo_input):
        if input == '':
            new_board = BingoBoard(bingo_input[idx+1:idx+6])
            bingo_boards.append(new_board)

    for number_called in bingo_numbers:
        for board in bingo_boards:
            x = board.CheckBoardAndRemove(number_called)
            if isinstance(x, BingoBoard) is False:
                return x

print(game_loop())