from random import randint


class Board:
    """
    
    """
    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["0" for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self. guesses = []
        self.ships = []

    

    