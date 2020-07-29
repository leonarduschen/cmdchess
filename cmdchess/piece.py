from abc import ABC, abstractmethod


class Piece(ABC):
    """Each piece is stored in tiles - which in turn is stored in a board layout attribute"""

    def __init__(self, color):
        self._color = color
        self.history = None

    @property
    def color(self):
        return self._color

    @property
    @abstractmethod
    def notation(self):
        pass

    @property
    @abstractmethod
    def hopping(self):
        pass

    @abstractmethod
    def generate_available_moves(self, position):
        pass

    @abstractmethod
    def generate_available_captures(self, position):
        pass


class King(Piece):
    def __init__(self, color):
        super().__init__(color)

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
    def __init__(self, color):
        super().__init__(color)

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
    def __init__(self, color):
        super().__init__(color)

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
    def __init__(self, color):
        super().__init__(color)

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
    def __init__(self, color):
        super().__init__(color)

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
    def __init__(self, color):
        super().__init__(color)
    
    @property
    def notation(self):
        return chr(9650)

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
        pass
