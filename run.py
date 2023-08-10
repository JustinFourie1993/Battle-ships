

class BattleshipGame:
    def __init__(self, board_size):
        self.board_size = board_size
        self.player_board = self.create_board()
        self.computer_board = self.create_board()
        self.computer_ships = self.place_ships(self.computer_board)
        self.player_ships = self.place_ships(self.player_board)

    def create_board(self):
        return [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]

    def place_ships(self, board):
        ships = []
        for _ in range(3):
            while True:
                x = random.randint(0, self.board_size - 1)
                y = random.randint(0, self.board_size - 1)
                if (x, y) not in ships:
                    ships.append((x, y))
                    break
        return ships

    