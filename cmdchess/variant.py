"""Variants module

"""

from abc import ABC, abstractmethod
from .piece import King, Queen, Bishop, Knight, Rook, Pawn
from .board import Board


class Variant(ABC):
    """Abstract-class for chess game variants (e.g. standard, chess960, Horde)

    """

    def __init__(self):
        self.board = Board()
        self._initialize_position()

    def make_move(self, from_, to_):
        """Make moves
        
        """
        if self._isvalidmove(from_, to_):
            self.board[to_].occupant = self.board[from_].occupant
            self.board[from_].occupant = None
        else:
            raise ValueError(f'Invalid Move: {from_} to {to_}')

    @abstractmethod
    def _isvalidmove(self, from_, to_):
        raise NotImplementedError()

    @abstractmethod
    def isfinished(self):
        """Check whether game is finished
        
        """
        raise NotImplementedError()

    @abstractmethod
    def _initialize_position(self):
        raise NotImplementedError()


class Standard(Variant):
    """Standard chess game
    
    """

    def _isvalidmove(self, from_, to_):
        return True

    def isfinished(self):
        return False

    def _initialize_position(self):
        self.board['A1'].occupant = Rook('W')
        self.board['B1'].occupant = Knight('W')
        self.board['C1'].occupant = Bishop('W')
        self.board['D1'].occupant = Queen('W')
        self.board['E1'].occupant = King('W')
        self.board['F1'].occupant = Bishop('W')
        self.board['G1'].occupant = Knight('W')
        self.board['H1'].occupant = Rook('W')
        self.board['A2'].occupant = Pawn('W')
        self.board['B2'].occupant = Pawn('W')
        self.board['C2'].occupant = Pawn('W')
        self.board['D2'].occupant = Pawn('W')
        self.board['E2'].occupant = Pawn('W')
        self.board['F2'].occupant = Pawn('W')
        self.board['G2'].occupant = Pawn('W')
        self.board['H2'].occupant = Pawn('W')
        self.board['A7'].occupant = Pawn('B')
        self.board['B7'].occupant = Pawn('B')
        self.board['C7'].occupant = Pawn('B')
        self.board['D7'].occupant = Pawn('B')
        self.board['E7'].occupant = Pawn('B')
        self.board['F7'].occupant = Pawn('B')
        self.board['G7'].occupant = Pawn('B')
        self.board['H7'].occupant = Pawn('B')
        self.board['A8'].occupant = Rook('B')
        self.board['B8'].occupant = Knight('B')
        self.board['C8'].occupant = Bishop('B')
        self.board['D8'].occupant = Queen('B')
        self.board['E8'].occupant = King('B')
        self.board['F8'].occupant = Bishop('B')
        self.board['G8'].occupant = Knight('B')
        self.board['H8'].occupant = Rook('B')


class Chess960(Variant):
    """Cheess960
    
    """


class Horde(Variant):
    """Horde chess
    
    """
