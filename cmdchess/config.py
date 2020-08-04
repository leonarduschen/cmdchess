"""Package-wide configuration settings"""

from colorama import Fore, Back

#Piece display settings
ASCII = {
    'WK': 'K',
    'WQ': 'Q',
    'WB': 'B',
    'WN': 'N',
    'WR': 'R',
    'WP': chr(9650),
    'BK': 'K',
    'BQ': 'Q',
    'BB': 'B',
    'BN': 'N',
    'BR': 'R',
    'BP': chr(9650)
}

UNICODE = {
    'WK': '♔',
    'WQ': '♕',
    'WB': '♗',
    'WN': '♘',
    'WR': '♖',
    'WP': '♙',
    'BK': '♚',
    'BQ': '♛',
    'BB': '♝',
    'BN': '♞',
    'BR': '♜',
    'BP': '♟'
}
class Config:
    def __init__(self, lightsqr, darksqr, whitepiece, blackpiece, symbols):
        self._lightsqr = lightsqr
        self._darksqr = darksqr
        self._whitepiece = whitepiece
        self._blackpiece = blackpiece
        self._symbols = symbols
    
    @property
    def lightsqr(self):
        return self._lightsqr
    
    @lightsqr.setter
    def lightsqr(self, value):
        self._lightsqr = value
    
    @property
    def darksqr(self):
        return self._darksqr
    
    @darksqr.setter
    def darksqr(self, value):
        self._darksqr = value
    
    @property
    def whitepiece(self):
        return self._whitepiece
    
    @whitepiece.setter
    def whitepiece(self, value):
        self._whitepiece = value

    @property
    def blackpiece(self):
        return self._blackpiece
    
    @blackpiece.setter
    def blackpiece(self, value):
        self._blackpiece = value

    @property
    def symbols(self):
        return self._symbols
    
    @symbols.setter
    def symbols(self, value):
        self._symbols = value

#Default configurations
configurations = Config(
    Back.WHITE,
    Back.BLACK,
    Fore.LIGHTWHITE_EX,
    Fore.LIGHTBLACK_EX,
    ASCII
)