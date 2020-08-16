"""Variants module

"""

from abc import ABC, abstractmethod
from .piece import King, Queen, Bishop, Knight, Rook, Pawn
from .board import Board, to_cartesian, to_algebraic


class MoveException(Exception):
    """Raised when making invalid moves

    """
    pass


class Variant(ABC):
    """Abstract-class for chess game variants (e.g. standard, chess960, Horde)

    """

    def __init__(self):
        self.board = Board()
        self._initialize_position()
        self.to_move = 'W'

    def change_color(self):
        if self.to_move == 'W':
            self.to_move = 'B'
        else:
            self.to_move = 'W'

    def make_move(self, from_, to_):
        """Make moves

        Parameters
        ----------
        from_: str
            Algebraic coordinate of the peice being moved
        to_ str:
            Algebraic coordinate of the destination square

        """
        if not self._isvalidmove(from_, to_):
            raise MoveException("Invalid move!")
        else:
            self.board[to_].occupant = self.board[from_].occupant
            self.board[from_].occupant = None
            self.change_color()

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
        if self.board[from_].occupant is None:
            print("Moving from empty square")
            return False  # moving from empty square
        piece = self.board[from_].occupant

        if piece.color != self.to_move:
            print("Wrong color")
            return False  # wrong piece color

        diff = (
            to_cartesian(to_)[0] - to_cartesian(from_)[0],
            to_cartesian(to_)[1] - to_cartesian(from_)[1]
        )

        if self.board[to_].occupant is not None:
            if piece.color == self.board[to_].occupant.color:
                print("Friendly attack")
                return False  # friendly attack

            if diff not in piece.get_captures():
                print("Invalid piece capture")
                return False  # invalid capture

            if not piece.hopping:
                pass

        if diff not in piece.get_moves():
            print("Invalid piece move")
            return False  # invalid move

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
