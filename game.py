from board import *


class Game:
    def __init__(self):
        self.board = Board()
        self.board.initialize_layout()

    def move(self, current, destination, verbose = False):
        self.board.layout[destination].place_piece(self.board.layout[current].occupant)
        self.board.layout[current].remove_piece()

        if verbose:
            print(f"\n \n Moving {self.board.layout[destination].notation} to {destination} \n \n")
        
        


    def evaluate_game(self):
        pass

if __name__ == "__main__":
    test_game = Game()
    test_game.board.display_layout()
    test_game.move("E2","E4", verbose = True)
    test_game.board.display_layout()
    test_game.move("E7","E5", verbose = True)
    test_game.board.display_layout()