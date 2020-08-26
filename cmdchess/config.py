"""Package-wide configuration settings

"""

from colorama import Fore, Back

# Piece display settings
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
    """A configuration container

    This class is imported on multiple modules and used as a package wide configuration settings

    Attributes
    ----------
    lightsqr
    darksqr
    whitepiece
    blackpiece
    symbols

    """

    def __init__(self, lightsqr, darksqr, whitepiece, blackpiece, symbols):
        """Initialization of config class

        Parameters
        ----------
        lightsqr: colorama.AnsiBack (e.g. colorama.Back.WHITE)
            display color of light squares
        darksqr: colorama.AnsiBack (e.g. colorama.Back.BLACK)
            display color of dark squares
        whitepiece: colorama.AnsiFore (e.g. colorama.Fore.WHITE)
            display color of white pieces
        blackpiece: colorama.AnsiFore (e.g. colorama.Fore.BLACK)
            display color of black pieces
        symbols: Symbols
            display symbols of both white and black pieces

        """
        self._lightsqr = lightsqr
        self._darksqr = darksqr
        self._whitepiece = whitepiece
        self._blackpiece = blackpiece
        self._symbols = symbols

    @property
    def lightsqr(self):
        """colorama.AnsiBack: color of light squares

        """
        return self._lightsqr

    @lightsqr.setter
    def lightsqr(self, value):
        self._lightsqr = value

    @property
    def darksqr(self):
        """colorama.AnsiBack: color of dark squares

        """
        return self._darksqr

    @darksqr.setter
    def darksqr(self, value):
        self._darksqr = value

    @property
    def whitepiece(self):
        """colorama.AnsiFore: color of white pieces

        """
        return self._whitepiece

    @whitepiece.setter
    def whitepiece(self, value):
        self._whitepiece = value

    @property
    def blackpiece(self):
        """colorama.AnsiFore: color of white pieces

        """
        return self._blackpiece

    @blackpiece.setter
    def blackpiece(self, value):
        self._blackpiece = value

    @property
    def symbols(self):
        """Symbols: symbols of both white and black pieces

        """
        return self._symbols

    @symbols.setter
    def symbols(self, value):
        self._symbols = value


# Default configurations
configurations = Config(
    Back.LIGHTCYAN_EX,
    Back.LIGHTBLACK_EX,
    Fore.LIGHTWHITE_EX,
    Fore.BLACK,
    ASCII
)
