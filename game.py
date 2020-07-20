from board import *


class Game:
    def __init__(self):
        self.board = self.Board()
        self.board.initialize_layout()
