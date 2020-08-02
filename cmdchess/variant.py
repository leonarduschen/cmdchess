from abc import ABC, abstractmethod
from cmdchess.piece import King, Queen, Bishop, Knight, Rook, Pawn
from cmdchess.board import Board, Tile

class Variant(ABC):
    def __init__(self):
        self.board = Board()
        self._initialize_position()

    def make_move(self, from_, to_):
        if self._isvalidmove(from_, to_):
            self.board.layout[to_].occupant = self.board.layout[from_].occupant
            self.board.layout[from_].occupant = None
        else:
            raise ValueError(f'Invalid Move')

    @abstractmethod
    def _isvalidmove(self, from_, to_):
        pass
    
    @abstractmethod
    def isfinished(self):
        pass

    @abstractmethod
    def _initialize_position(self):
        pass

class Standard(Variant):
    def __init__(self):
        super().__init__()

    def _isvalidmove(self, from_, to_):
        return True

    def isfinished(self):
        return False

    def _initialize_position(self):
        self.board.layout['A1'].ocupant = Rook('W')
        self.board.layout['B1'].ocupant = Knight('W')
        self.board.layout['C1'].ocupant = Bishop('W')
        self.board.layout['D1'].ocupant = Queen('W')
        self.board.layout['E1'].ocupant = King('W')
        self.board.layout['F1'].ocupant = Bishop('W')
        self.board.layout['G1'].ocupant = Knight('W')
        self.board.layout['H1'].ocupant = Rook('W')

        self.board.layout['A2'].ocupant = Pawn('W')
        self.board.layout['B2'].ocupant = Pawn('W')
        self.board.layout['C2'].ocupant = Pawn('W')
        self.board.layout['D2'].ocupant = Pawn('W')
        self.board.layout['E2'].ocupant = Pawn('W')
        self.board.layout['F2'].ocupant = Pawn('W')
        self.board.layout['G2'].ocupant = Pawn('W')
        self.board.layout['H2'].ocupant = Pawn('W')

        self.board.layout['A7'].ocupant = Pawn('B')
        self.board.layout['B7'].ocupant = Pawn('B')
        self.board.layout['C7'].ocupant = Pawn('B')
        self.board.layout['D7'].ocupant = Pawn('B')
        self.board.layout['E7'].ocupant = Pawn('B')
        self.board.layout['F7'].ocupant = Pawn('B')
        self.board.layout['G7'].ocupant = Pawn('B')
        self.board.layout['H7'].ocupant = Pawn('B')

        self.board.layout['A8'].ocupant = Rook('B')
        self.board.layout['B8'].ocupant = Knight('B')
        self.board.layout['C8'].ocupant = Bishop('B')
        self.board.layout['D8'].ocupant = Queen('B')
        self.board.layout['E8'].ocupant = King('B')
        self.board.layout['F8'].ocupant = Bishop('B')
        self.board.layout['G8'].ocupant = Knight('B')
        self.board.layout['H8'].ocupant = Rook('B')

class Chess960(Variant):
    def __init__(self):
        super().__init__()

class Horde(Variant):
    def __init__(self):
        super().__init__()

