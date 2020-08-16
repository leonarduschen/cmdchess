"""Piece module

"""

from abc import ABC, abstractmethod
from .config import configurations


class Piece(ABC):
    """Abstract-class for standard (including pawn) and custom chess pieces

    At any point of time, a piece instance is stored in a square instance - which in turn is stored in a board instance

    Attributes
    ----------
    color
    position
    notation
    hopping

    """

    def __init__(self, color, position=None):
        """Initialization of a piece instance

        Parameters
        ----------
        color: {'W', 'B'}
            Piece color
        position: str, optional
            Algebraic notation of current position (e.g. A1)

        """
        self._color = color
        self._position = position

    def __repr__(self):
        return self.color + self.notation

    def __str__(self):
        if self.color == 'W':
            foreground = configurations.whitepiece
        else:
            foreground = configurations.blackpiece
        symbol = configurations.symbols[self.color + self.notation]
        return foreground + symbol

    @property
    def color(self):
        """str: Piece color of either 'W' or 'B'

        """
        return self._color

    @property
    def position(self):
        """str: Algebraic notatio of current position (e.g. A1)

        """
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    @abstractmethod
    def notation(self):
        """str: Algebraic notation (e.g. 'K', 'Q', 'B', 'N', 'R', 'P')

        """
        raise NotImplementedError()

    @property
    @abstractmethod
    def hopping(self):
        """bool: Ability to ignore blocking pieces

        """
        raise NotImplementedError()

    @abstractmethod
    def get_moves(self):
        """Return available moves relative to current position

        Note
        ----
        Does not take into account other pieces

        Returns
        -------
        obj:'list' of obj:'tuple' of obj:'int'
            Available moves in cartesian coordinate

        """
        raise NotImplementedError()

    @abstractmethod
    def get_captures(self):
        """Return available captures relative to current position

        Note
        ----
        Does not take into account other pieces. Standard pieces have the exact same captures as moves except for pawns.

        Returns
        -------
        obj:'list' of obj:'tuple' of obj:'int'
            Available moves in cartesian coordinate

        """
        raise NotImplementedError()


class King(Piece):
    """King class

    """
    @property
    def notation(self):
        return 'K'

    @property
    def hopping(self):
        return False

    def get_moves(self):
        hor = [-1, 0, 1]
        ver = [-1, 0, 1]
        combination = [(i, j) for i in hor for j in ver]
        combination = set(combination)
        combination.remove((0, 0))
        return combination

    def get_captures(self):
        hor = [-1, 0, 1]
        ver = [-1, 0, 1]
        combination = [(i, j) for i in hor for j in ver]
        combination = set(combination)
        combination.remove((0, 0))
        return combination


class Queen(Piece):
    """Queen class

    """
    @property
    def notation(self):
        return 'Q'

    @property
    def hopping(self):
        return False

    def get_moves(self):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = (
            [(i, j) for i, j in zip(hor, ver)] +
            [(i, 0) for i in hor] +
            [(0, j) for j in ver]
        )
        combination = set(combination)
        combination = combination.remove((0, 0))
        return combination

    def get_captures(self):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = (
            [(i, j) for i, j in zip(hor, ver)] +
            [(i, 0) for i in hor] +
            [(0, j) for j in ver]
        )
        combination = set(combination)
        combination = combination.remove((0, 0))
        return combination


class Bishop(Piece):
    """Bishop class

    """
    @property
    def notation(self):
        return 'B'

    @property
    def hopping(self):
        return False

    def get_moves(self):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, j) for i, j in zip(hor, ver)]
        combination = set(combination)
        combination = combination.remove((0, 0))
        return combination

    def get_captures(self):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, j) for i, j in zip(hor, ver)]
        combination = set(combination)
        combination = combination.remove((0, 0))
        return combination


class Knight(Piece):
    """Knight class

    """
    @property
    def notation(self):
        return 'N'

    @property
    def hopping(self):
        return True

    def get_moves(self):
        combination = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                       (1, -2), (2, -1), (-1, -2), (-2, -1)]
        combination = set(combination)
        return combination

    def get_captures(self):
        combination = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                       (1, -2), (2, -1), (-1, -2), (-2, -1)]
        combination = set(combination)
        return combination


class Rook(Piece):
    """Rook class

    """
    @property
    def notation(self):
        return 'R'

    @property
    def hopping(self):
        return False

    def get_moves(self):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, 0) for i in hor] + [(0, j) for j in ver]
        combination = set(combination)
        combination.remove((0, 0))
        return combination

    def get_captures(self):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, 0) for i in hor] + [(0, j) for j in ver]
        combination = set(combination)
        combination.remove((0, 0))
        return combination


class Pawn(Piece):
    """Pawn class

    """

    def __init__(self, color, position=None, double_advance=True):
        """Pawn initialization

        Parameters
        ----------
        color: str
            Piece color of either 'W' or 'B'
        double_advance: bool, optional
            Enable first-move double-advancement

        """

        super().__init__(color, position)
        self.double_advance = double_advance

    @property
    def notation(self):
        return 'P'

    @property
    def hopping(self):
        return False

    def get_moves(self):
        if self.color == 'W':
            combination = [(0, 1)]
            if self.double_advance:
                combination += [(0, 2)]

        if self.color == 'B':
            combination = [(0, -1)]
            if self.double_advance:
                combination += [(0, -2)]
        combination = set(combination)
        return combination

    def get_captures(self):
        if self.color == 'W':
            combination = [(-1, 1), (1, 1)]

        if self.color == 'B':
            combination = [(-1, -1), (1, -1)]

        combination = set(combination)
        return combination

    def promote(self):
        """Pawn promotion

        """
        return False
