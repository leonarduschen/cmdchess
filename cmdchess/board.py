from colorama import Fore, Back, Style
from cmdchess.piece import King, Queen, Bishop, Knight, Rook, Pawn
from cmdchess.tile import Tile


class Board:
    """A board layout consists of 64 tiles stored in the attribute layout as a dictionary. A tile in turn can be occupied by a piece"""

    def __init__(self):
        self.layout = self.__generate_empty_layout()

    def __generate_empty_layout(self):
        empty_layout = dict()
        for ranks in ['1', '2', '3', '4', '5', '6', '7', '8']:
            for files in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                empty_layout[files + ranks] = Tile(files + ranks)
        return empty_layout

    def generate_standard_layout(self, algebraic=True):
        self.layout['A1'].place_piece(Rook('W'))
        self.layout['B1'].place_piece(Knight('W'))
        self.layout['C1'].place_piece(Bishop('W'))
        self.layout['D1'].place_piece(Queen('W'))
        self.layout['E1'].place_piece(King('W'))
        self.layout['F1'].place_piece(Bishop('W'))
        self.layout['G1'].place_piece(Knight('W'))
        self.layout['H1'].place_piece(Rook('W'))

        self.layout['A2'].place_piece(Pawn('W'))
        self.layout['B2'].place_piece(Pawn('W'))
        self.layout['C2'].place_piece(Pawn('W'))
        self.layout['D2'].place_piece(Pawn('W'))
        self.layout['E2'].place_piece(Pawn('W'))
        self.layout['F2'].place_piece(Pawn('W'))
        self.layout['G2'].place_piece(Pawn('W'))
        self.layout['H2'].place_piece(Pawn('W'))

        self.layout['A7'].place_piece(Pawn('B'))
        self.layout['B7'].place_piece(Pawn('B'))
        self.layout['C7'].place_piece(Pawn('B'))
        self.layout['D7'].place_piece(Pawn('B'))
        self.layout['E7'].place_piece(Pawn('B'))
        self.layout['F7'].place_piece(Pawn('B'))
        self.layout['G7'].place_piece(Pawn('B'))
        self.layout['H7'].place_piece(Pawn('B'))

        self.layout['A8'].place_piece(Rook('B'))
        self.layout['B8'].place_piece(Knight('B'))
        self.layout['C8'].place_piece(Bishop('B'))
        self.layout['D8'].place_piece(Queen('B'))
        self.layout['E8'].place_piece(King('B'))
        self.layout['F8'].place_piece(Bishop('B'))
        self.layout['G8'].place_piece(Knight('B'))
        self.layout['H8'].place_piece(Rook('B'))
    
    def __get_colored_notation(self, key):
        if self.layout[key].occupant is None:
            return f"{self.layout[key].notation}"

        elif self.layout[key].occupant.color == 'W':
            return Fore.WHITE + Style.BRIGHT + f"{self.layout[key].notation}"
        else:
            return Fore.BLACK + Style.BRIGHT + f"{self.layout[key].notation}"
    
    def display_layout(self):
        color_idx = 0
        for ranks in ['8', '7', '6', '5', '4', '3', '2', '1']:
            for files in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                key = files + ranks
                if color_idx % 2 == 0:
                    print(Back.WHITE, self.__get_colored_notation(key), end=" ")
                else:
                    print(Back.BLACK, self.__get_colored_notation(key), end=" ")
                if files == 'H':
                    print(Style.RESET_ALL, "|")
                    color_idx += 1
                color_idx += 1
    



    @staticmethod
    def to_cartesian(algebraic):
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

    @staticmethod
    def to_algebraic(cartesian):
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
