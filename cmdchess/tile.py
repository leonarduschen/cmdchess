class Tile:
    """Tiles makes up board layout. At any point of time, a tile can either be occupied by a piece or be vacant"""

    def __init__(self, position):
        self.position = position
        self.occupant = None
        self.notation = "--"

    def place_piece(self, piece):
        self.occupant = piece
        self.notation = piece.notation

    def remove_piece(self):
        self.occupant = None
        self.notation = "--"
