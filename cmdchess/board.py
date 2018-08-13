"""Board module

"""

from colorama import Style
from .config import configurations


class Square:
    """Squares makes up board layout. At any point of time, a square can either be occupied by a piece or be vacant
    
    Attributes
    ----------
    position
    color
    occupant

    """

    def __init__(self, position, color):
        """Initialization of a square instance

        Parameters
        ----------
        position: str
            Algebraic coordinate of current position (e.g. 'A1')
        color: {'dark', 'light'}
            Square color

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
    """Composition of 64 individual square instances.

    The class may be treated as a dictionary with chess board algebraic notatation as its keys (e.g. A1).

    """
    __slots__ = (
        'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8',
        'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7',
        'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
        'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
        'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
        'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
        'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
        'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
    )

    def __init__(self):
        color = ['dark', 'light']
        idx = 0
        for attribute in self.__slots__:
            idx += 1
            setattr(self, attribute, Square(attribute, color[idx % 2]))
            if attribute[0] == 'H':
                idx += 1

    def __getitem__(self, key):
        return getattr(self, key)

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __iter__(self):
        return iter(self.__slots__)

    def keys(self):
        """Return keys
        
        """
        return self.__slots__

    def items(self):
        """Return all items
        
        """
        for attribute in self.__slots__:
            yield attribute, getattr(self, attribute)

    def display_layout(self):
        """Display current state of the board
        
        """
        for square in self.__slots__:
            if square[0] == 'H':
                print(self[square])
            else:
                print(self[square], end="")
        print(Style.RESET_ALL)


def to_cartesian(algebraic):
    """Convert algebraic to cartesian
    
    """
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
    """Convert cartesian to algebraic
    
    """
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
