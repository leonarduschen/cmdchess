"""Chess variants module"""

from abc import ABC, abstractmethod
from .piece import King, Queen, Bishop, Knight, Rook, Pawn
from .board import Board


class Variant(ABC):
    """Abstract-class for standard (including pawn) and custom chess pieces

    At any point of time, a piece instance is stored in a square instance - which in turn is stored in a board instance

    """

    def __init__(self):
        self.board = Board()
        self._initialize_position()
        # self._display = display

    def make_move(self, from_, to_):
        """Make moves"""
        if self._isvalidmove(from_, to_):
            self.board.layout[to_].occupant = self.board.layout[from_].occupant
            self.board.layout[from_].occupant = None
        else:
            raise ValueError(f'Invalid Move: {from_} to {to_}')

    @abstractmethod
    def _isvalidmove(self, from_, to_):
        pass

    @abstractmethod
    def isfinished(self):
        """Check whether game is finished"""

    @abstractmethod
    def _initialize_position(self):
        pass


class Standard(Variant):
    """Standard chess game"""

    def _isvalidmove(self, from_, to_):
        return True

    def isfinished(self):
        return False

    def _initialize_position(self):
        self.board.layout['A1'].occupant = Rook('W')
        self.board.layout['B1'].occupant = Knight('W')
        self.board.layout['C1'].occupant = Bishop('W')
        self.board.layout['D1'].occupant = Queen('W')
        self.board.layout['E1'].occupant = King('W')
        self.board.layout['F1'].occupant = Bishop('W')
        self.board.layout['G1'].occupant = Knight('W')
        self.board.layout['H1'].occupant = Rook('W')

        self.board.layout['A2'].occupant = Pawn('W')
        self.board.layout['B2'].occupant = Pawn('W')
        self.board.layout['C2'].occupant = Pawn('W')
        self.board.layout['D2'].occupant = Pawn('W')
        self.board.layout['E2'].occupant = Pawn('W')
        self.board.layout['F2'].occupant = Pawn('W')
        self.board.layout['G2'].occupant = Pawn('W')
        self.board.layout['H2'].occupant = Pawn('W')

        self.board.layout['A7'].occupant = Pawn('B')
        self.board.layout['B7'].occupant = Pawn('B')
        self.board.layout['C7'].occupant = Pawn('B')
        self.board.layout['D7'].occupant = Pawn('B')
        self.board.layout['E7'].occupant = Pawn('B')
        self.board.layout['F7'].occupant = Pawn('B')
        self.board.layout['G7'].occupant = Pawn('B')
        self.board.layout['H7'].occupant = Pawn('B')

        self.board.layout['A8'].occupant = Rook('B')
        self.board.layout['B8'].occupant = Knight('B')
        self.board.layout['C8'].occupant = Bishop('B')
        self.board.layout['D8'].occupant = Queen('B')
        self.board.layout['E8'].occupant = King('B')
        self.board.layout['F8'].occupant = Bishop('B')
        self.board.layout['G8'].occupant = Knight('B')
        self.board.layout['H8'].occupant = Rook('B')


class Chess960(Variant):
    """Cheess960"""


class Horde(Variant):
    """Horde chess"""
