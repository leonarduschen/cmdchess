from board import Board
from piece import King, Queen, Bishop, Knight, Rook, Pawn
from tile import Tile
from coordinates import to_cartesian, to_algebraic


class Game:
    def __init__(self):
        self.board = Board()
        self.board.initialize_layout()

    def make_move(self, current, destination, verbose = False):
        if self.isValidMove(current, destination):
            self.board.layout[destination].place_piece(self.board.layout[current].occupant)
            self.board.layout[current].remove_piece()

        if verbose:
            print(f"\n \n Moving {self.board.layout[destination].notation} to {destination} \n \n")
        
    def isValidMove(self, current, destination, verbose = False):
        isValidPieceMove = to_cartesian(destination) in self.board.layout[current].occupant.generate_available_moves(to_cartesian(current))
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
    test_game = Game()
    test_game.board.display_layout()
    test_game.make_move("E2","E4", verbose = True)
    test_game.board.display_layout()
    test_game.make_move("E7","E5", verbose = True)
    test_game.board.display_layout()