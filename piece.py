class Piece:
    """Each piece is stored in tiles - which in turn is stored in a board layout attribute"""
    def __init__(self, color):
        self.color = color
        self.history = None


class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.notation = 'K'

    def generate_available_moves(self, position):
        hor = [-1, 0, 1]
        ver = [-1, 0, 1]
        combination = [(i, j) for i in hor for j in ver]
        return [position + i*10 + j for i, j in combination]


class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.notation = 'Q'

    def generate_available_moves(self, position):
        hor = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, j) for i, j in zip(hor, ver)] + [(i, 0)
                                                            for i in hor] + [(0, j) for j in ver]
        return [position + i*10 + j for i, j in combination]


class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.notation = 'B'

    def generate_available_moves(self, position):
        hor = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, j) for i, j in zip(hor, ver)]
        return [position + i*10 + j for i, j in combination]


class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.notation = 'N'

    def generate_available_moves(self, position):
        combination = [(1, 2), (2, 1), (-1, 2), (-2, 1),
                       (1, -2), (2, -1), (-1, -2), (-2, -1)]
        return [position + i*10 + j for i, j in combination]


class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.notation = 'R'

    def generate_available_moves(self, position):
        hor = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        ver = [-8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8]
        combination = [(i, 0) for i in hor] + [(0, j) for j in ver]
        return [position + i*10 + j for i, j in combination]


class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.notation = 'P'

    def generate_available_moves(self, position):
        combination = (0, 1)
        return [position + i*10 + j for i, j in combination]

    def promote(self):
        pass
