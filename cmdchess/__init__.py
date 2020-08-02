from cmdchess.game import main
from colorama import Fore, Back, Style


#Unicode Console
unicode_console = False

#Piece display settings
ASCII_WHITE = Style.BRIGHT + Fore.LIGHTWHITE_EX
ASCII_BLACK = Style.BRIGHT + Fore.LIGHTBLACK_EX
ASCII = {
    'WK': ASCII_WHITE + 'K',
    'WQ': ASCII_WHITE + 'Q',
    'WB': ASCII_WHITE + 'B',
    'WN': ASCII_WHITE + 'N',
    'WR': ASCII_WHITE + 'R',
    'WP': ASCII_WHITE + chr(960),
    'BK': ASCII_BLACK + 'K',
    'BQ': ASCII_BLACK + 'Q',
    'BB': ASCII_BLACK + 'B',
    'BN': ASCII_BLACK + 'N',
    'BR': ASCII_BLACK + 'R',
    'BP': ASCII_BLACK + chr(960)
}

UNICODE_COLOR = Style.BRIGHT + Fore.LIGHTBLACK_EX
UNICODE = {
    'WK': UNICODE_COLOR + '♔',
    'WQ': UNICODE_COLOR + '♕',
    'WB': UNICODE_COLOR + '♗',
    'WN': UNICODE_COLOR + '♘',
    'WR': UNICODE_COLOR + '♖',
    'WP': UNICODE_COLOR + '♙',
    'BK': UNICODE_COLOR + '♚',
    'BQ': UNICODE_COLOR + '♛',
    'BB': UNICODE_COLOR + '♝',
    'BN': UNICODE_COLOR + '♞',
    'BR': UNICODE_COLOR + '♜',
    'BP': UNICODE_COLOR + '♟'
}

if unicode_console:
    piece_display = UNICODE
else:
    piece_display = ASCII

#Tile Settings
light_tiles = Back.WHITE
dark_tiles = Back.BLACK

def cmdchess():
    main()
