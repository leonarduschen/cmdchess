from piece import King, Queen, Bishop, Knight, Rook, Pawn


class Tile:
    """Tiles makes up board layout. At any point of time, a tile can either be occupied by a piece or be vacant"""

    def __init__(self, position):
        self.position = position
        self.occupant = None
        self.notation = "-"

    def place_piece(self, piece):
        self.occupant = piece
        self.notation = piece.notation

    def remove_piece(self):
        self.occupant = None
        self.notation = "-"


class Board:
    """A board layout consists of 64 tiles stored in the attribute layout as a dictionary. A tile in turn can be occupied by a piece"""
    def __init__(self):
        self.layout = self.generate_empty_layout()

    def generate_empty_layout(self):
        empty_layout = dict()
        for ranks in ['1', '2', '3', '4', '5', '6', '7', '8']:
            for files in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                empty_layout[files + ranks] = Tile(files + ranks)
        return empty_layout

    def initialize_layout(self):
        self.layout['A1'].place_piece(Rook('White'))
        self.layout['B1'].place_piece(Knight('White'))
        self.layout['C1'].place_piece(Bishop('White'))
        self.layout['D1'].place_piece(King('White'))
        self.layout['E1'].place_piece(Queen('White'))
        self.layout['F1'].place_piece(Bishop('White'))
        self.layout['G1'].place_piece(Knight('White'))
        self.layout['H1'].place_piece(Rook('White'))

        self.layout['A2'].place_piece(Pawn('White'))
        self.layout['B2'].place_piece(Pawn('White'))
        self.layout['C2'].place_piece(Pawn('White'))
        self.layout['D2'].place_piece(Pawn('White'))
        self.layout['E2'].place_piece(Pawn('White'))
        self.layout['F2'].place_piece(Pawn('White'))
        self.layout['G2'].place_piece(Pawn('White'))
        self.layout['H2'].place_piece(Pawn('White'))

        self.layout['A7'].place_piece(Pawn('Black'))
        self.layout['B7'].place_piece(Pawn('Black'))
        self.layout['C7'].place_piece(Pawn('Black'))
        self.layout['D7'].place_piece(Pawn('Black'))
        self.layout['E7'].place_piece(Pawn('Black'))
        self.layout['F7'].place_piece(Pawn('Black'))
        self.layout['G7'].place_piece(Pawn('Black'))
        self.layout['H7'].place_piece(Pawn('Black'))

        self.layout['A8'].place_piece(Rook('Black'))
        self.layout['B8'].place_piece(Knight('Black'))
        self.layout['C8'].place_piece(Bishop('Black'))
        self.layout['D8'].place_piece(King('Black'))
        self.layout['E8'].place_piece(Queen('Black'))
        self.layout['F8'].place_piece(Bishop('Black'))
        self.layout['G8'].place_piece(Knight('Black'))
        self.layout['H8'].place_piece(Rook('Black'))

    def display_layout(self):
        for ranks in ['8', '7', '6', '5', '4', '3', '2', '1']:
            for files in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                key = files + ranks
                print(f"{self.layout[key].notation} ", end="")
                if files == 'H':
                    print("")
