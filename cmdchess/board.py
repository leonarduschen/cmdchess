"""Board module"""

from colorama import Style
from .config import configurations


class Square:
    """Squares makes up board layout. At any point of time, a square can either be occupied by a piece or be vacant"""

    def __init__(self, position, color):
        """Initialization of a square instance

        Parameters
        ----------
        position: str
            Algebraic coordinate of current position (e.g. 'A1')
        color: str
            Piece color of either 'W' or 'B'

        """
        self._position = position
        self._color = color
        self._occupant = None

    def __repr__(self):
        return f'{self.color} {repr(self.occupant)} {self.position}'

    def __str__(self):
        if self.color == 'light':
            background = configurations.lightsqr
        else:
            background = configurations.darksqr

        if self.occupant is None:
            return background + '   '
        return background + f' {str(self.occupant)} '

    @property
    def position(self):
        """str: Algebraic coordinate of current position (e.g. 'A1')"""
        return self._position

    @property
    def color(self):
        """str: Square color of either 'W' or 'B'"""
        return self._color

    @property
    def occupant(self):
        """Piece: An instance of piece or None"""
        return self._occupant

    @occupant.setter
    def occupant(self, piece):
        self._occupant = piece


class Board:
    """Composition of 64 individual square objects and multiple Piece objects.

    Attributes:
    ----------
    layout (dict): Contains square objects
    """

    def __init__(self):
        self.layout = self._initialize_layout()

    def _initialize_layout(self):
        layout = dict()
        color = ['dark', 'light']
        idx = 0

        for rank_ in ['1', '2', '3', '4', '5', '6', '7', '8']:
            idx += 1
            for file_ in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                idx += 1
                layout[file_ + rank_] = Square(file_ + rank_, color[idx % 2])
        return layout

    def display_layout(self):
        """Display layout"""
        for rank_ in ['8', '7', '6', '5', '4', '3', '2', '1']:
            for file_ in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                if file_ == 'H':
                    print(str(self.layout[file_ + rank_]))
                else:
                    print(str(self.layout[file_ + rank_]), end="")
        print(Style.RESET_ALL)


def to_cartesian(algebraic):
    """Convert algebraic to cartesian"""
    mapper = {
        'A': 1,
        'B': 2,
        'C': 3,
        'D': 4,
        'E': 5,
        'F': 6,
        'G': 7,
        'H': 8}

    hor = mapper[algebraic[0]]
    ver = int(algebraic[1])

    return (hor, ver)


def to_algebraic(cartesian):
    """Convert cartesian to algebraic"""
    mapper = {
        1: 'A',
        2: 'B',
        3: 'C',
        4: 'D',
        5: 'E',
        6: 'F',
        7: 'G',
        8: 'H'}

    files = mapper[cartesian[0]]
    rank = str(cartesian[1])

    return files + rank
