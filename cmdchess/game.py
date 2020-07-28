import os
from board import Board


class Game:
    def __init__(self):
        self.board = Board()
        self.board.generate_standard_layout()

    def make_move(self, current, destination, verbose=False):
        if self.isValidMove(current, destination):
            self.board.layout[destination].place_piece(
                self.board.layout[current].occupant)
            self.board.layout[current].remove_piece()

        if verbose:
            print(
                f"\n \n Moving {self.board.layout[destination].notation} to {destination} \n \n")

    def isValidMove(self, current, destination, verbose=False):
        isValidPieceMove = Board.to_cartesian(
            destination) in self.board.layout[current].occupant.generate_available_moves(Board.to_cartesian(current))
        isValidBoardMove = destination in self.board.layout.keys()
        isPathwayClear = True
        isNotFriendlyCapture = True

        if verbose:
            print(f'Valid Piece Move: {isValidPieceMove}')
            print(f'Valid Board Move: {isValidBoardMove}')
            print(f'Pathway Clear: {isPathwayClear}')
            print(f'Capturing Friendly: {isNotFriendlyCapture}')

        return isValidPieceMove & isValidBoardMove & isPathwayClear & isNotFriendlyCapture

    def evaluate_game(self):
        pass


if __name__ == "__main__":
    game = Game()
    game.board.display_layout()
    while True:
        current = input("Move from: ")
        destination = input("Move to: ")
        os.system('cls')
        print(f'Moving {current} to {destination}')
        game.make_move(current, destination, verbose=True)
        game.board.display_layout()