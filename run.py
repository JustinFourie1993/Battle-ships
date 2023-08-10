board = []

for i in range(5):
    board.append(["0"]*5)

def make_grid(board):
    for i in board:
        print(" ".join(i))

make_grid(board)

