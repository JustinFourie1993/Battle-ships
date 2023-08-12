import random


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

    def print_board(self, board):
        print("  " + " ".join([str(i) for i in range(1, self.board_size + 1)]))
        for i, row in enumerate(board):
            print(chr(ord('A') + i) + " " + " ".join(row))

    def get_player_guess(self):
        while True:
            guess = input("Enter your guess (e.g., A1): ").upper()
            if len(guess) != 2 or not ('A' <= guess[0] <= chr(ord('A') + self.board_size - 1)) or not ('1' <= guess[1] <= str(self.board_size)):
                print("Invalid guess. Please try again.")
                continue
            y = ord(guess[0]) - ord('A')
            x = int(guess[1]) - 1
            return x, y

    def get_computer_guess(self):
        x = random.randint(0, self.board_size - 1)
        y = random.randint(0, self.board_size - 1)
        return x, y

    def process_guess(self, board, ships, guess):
        x, y = guess
        if (x, y) in ships:
            print("Hit!")
            board[y][x] = 'H'
            ships.remove((x, y))
        else:
            print("Miss!")
            board[y][x] = 'M'

    def check_winner(self, ships):
        return len(ships) == 0

    def play(self):
        print("Let's play Battleship!")
        while True:
            print("Your board:")
            self.print_board(self.player_board)
            print("Computer's board:")
            self.print_board(self.computer_board)

            player_guess = self.get_player_guess()
            self.process_guess(self.computer_board, self.computer_ships, player_guess)

            if self.check_winner(self.computer_ships):
                print("Congratulations! You sunk all the computer's ships. You win!")
                break

            computer_guess = self.get_computer_guess()
            self.process_guess(self.player_board, self.player_ships, computer_guess)

            if self.check_winner(self.player_ships):
                print("Oh no! The computer sunk all your ships. You lose!")
                break

# Start the game
if __name__ == "__main__":
    game = BattleshipGame(board_size=5)
    game.play()
