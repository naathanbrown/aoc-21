class BingoBoard:
    def __init__(self, input):
        self.board = [[],[],[],[],[]]
        for i in range(0, 5):
            self.board[i] = list(map(int,list(filter(None, input[i].split(' ')))))

    def SumBoard(self, number):
        score = 0
        for row in self.board:
            score += sum(row)
        return score * number

    def CheckBoardAndRemove(self, number):
        for idx, row in enumerate(self.board):
            row = [x for x in row if x != number]
            self.board[idx] = row
        return self.CheckWinner(number)

    def CheckWinner(self, number):
        for row in self.board:
            if len(row) == 0:
                return self.SumBoard(number)
            else:
                return self

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