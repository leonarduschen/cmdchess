"""Piece module"""

from abc import ABC, abstractmethod
from .config import configurations


class Piece(ABC):
    """Abstract-class for standard (including pawn) and custom chess pieces

    At any point of time, a piece instance is stored in a tile instance - which in turn is stored in a board instance
    """

    def __init__(self, color):
        """Initialization of a piece instance

        Parameters
        ----------
        color: str
            Piece color of either 'W' or 'B'

        """
        self._color = color

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
        """str: Piece color of either 'W' or 'B'"""
        return self._color

    @property
    @abstractmethod
    def notation(self):
        """str: Algebraic notation (e.g. 'K', 'Q', 'B', 'N', 'R', 'P')"""

    @property
    @abstractmethod
    def hopping(self):
        """bool: Ability to ignore blocking pieces"""

    @abstractmethod
    def generate_available_moves(self, position):
        """Return available moves relative to current position

        Note
        ----
        Does not take into account other pieces

        Parameters
        ----------
        position: obj:'tuple' of obj:'int'
            Cartesian coordinate of current position (e.g. (5, 8))

        Returns
        -------
        obj:'list' of obj:'tuple' of obj:'int'
            Available moves in cartesian coordinate

        """

    @abstractmethod
    def generate_available_captures(self, position):
        """Return available captures relative to current position

        Note
        ----
        Does not take into account other pieces. Standard pieces have the exact same captures as moves except for pawns.

        Parameters
        ----------
        position: obj:'tuple' of obj:'int'
            Cartesian coordinate of current position (e.g. (5, 8))

        Returns
        -------
        obj:'list' of obj:'tuple' of obj:'int'
            Available moves in cartesian coordinate

        """


class King(Piece):
    """King class, notation: K"""
    @property
    def notation(self):
        return 'K'

    @property
    def hopping(self):
        return False

    def generate_available_moves(self, position):
        hor = [-1, 0, 1]
        ver = [-1, 0, 1]
        combination = [(i, j) for i in hor for j in ver]
        combination.remove((0, 0))
        return [(position[0] + i, position[1] + j)
                for i, j in combination]

    def generate_available_captures(self, position):
        hor = [-1, 0, 1]
        ver = [-1, 0, 1]
        combination = [(i, j) for i in hor for j in ver]
        combination.remove((0, 0))
        return [(position[0] + i, position[1] + j)
                for i, j in combination]


class Queen(Piece):
    """Queen class, notation: Q"""
    @property
    def notation(self):
        return 'Q'

    @property
    def hopping(self):
        return False

    def generate_available_moves(self, position):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = (
            [(i, j) for i, j in zip(hor, ver)] +
            [(i, 0) for i in hor] +
            [(0, j) for j in ver]
        )
        combination = combination.remove((0, 0))
        return [(position[0] + i, position[1] + j)
                for i, j in combination]

    def generate_available_captures(self, position):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = (
            [(i, j) for i, j in zip(hor, ver)] +
            [(i, 0) for i in hor] +
            [(0, j) for j in ver]
        )
        combination = combination.remove((0, 0))
        return [(position[0] + i, position[1] + j)
                for i, j in combination]


class Bishop(Piece):
    """Bishop class, notation: B"""
    @property
    def notation(self):
        return 'B'

    @property
    def hopping(self):
        return False

    def generate_available_moves(self, position):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, j) for i, j in zip(hor, ver)]
        combination = combination.remove((0, 0))
        return [(position[0] + i, position[1] + j)
                for i, j in combination]

    def generate_available_captures(self, position):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, j) for i, j in zip(hor, ver)]
        combination = combination.remove((0, 0))
        return [(position[0] + i, position[1] + j)
                for i, j in combination]


class Knight(Piece):
    """Knight class, notation: N"""
    @property
    def notation(self):
        return 'N'

    @property
    def hopping(self):
        return True

    def generate_available_moves(self, position):
        combination = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                       (1, -2), (2, -1), (-1, -2), (-2, -1)]
        return [(position[0] + i, position[1] + j)
                for i, j in combination]

    def generate_available_captures(self, position):
        combination = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                       (1, -2), (2, -1), (-1, -2), (-2, -1)]
        return [(position[0] + i, position[1] + j)
                for i, j in combination]


class Rook(Piece):
    """Rook class, notation: R"""
    @property
    def notation(self):
        return 'R'

    @property
    def hopping(self):
        return False

    def generate_available_moves(self, position):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, 0) for i in hor] + [(0, j) for j in ver]
        combination.remove((0, 0))
        return [(position[0] + i, position[1] + j)
                for i, j in combination]

    def generate_available_captures(self, position):
        hor = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -
               2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, 0) for i in hor] + [(0, j) for j in ver]
        combination.remove((0, 0))
        return [(position[0] + i, position[1] + j)
                for i, j in combination]


class Pawn(Piece):
    """Pawn class, notation: P"""
    @property
    def notation(self):
        return 'P'

    @property
    def hopping(self):
        return False

    def generate_available_moves(self, position):
        if self.color == 'W':
            combination = [(0, 1)]
            if position[1] == 2:
                combination += [(0, 2)]

        if self.color == 'B':
            combination = [(0, -1)]
            if position[1] == 7:
                combination += [(0, -2)]

        return [(position[0] + i, position[1] + j)
                for i, j in combination]

    def generate_available_captures(self, position):
        if self.color == 'W':
            combination = [(-1, 1), (1, 1)]

        if self.color == 'B':
            combination = [(-1, -1), (1, -1)]

        return [(position[0] + i, position[1] + j)
                for i, j in combination]

    def promote(self):
        """Pawn promotion"""
        return False
