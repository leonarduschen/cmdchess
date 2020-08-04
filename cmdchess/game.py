"""Game module"""

import os
from .variant import Standard
from .config import configurations


def main(ASCII = True):
    if ASCII:
        configurations.symbols = {
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
    
    game = Standard()
    while True:
        os.system('cls')
        game.board.display_layout()
        print(" ")
        move = input("Move: ")

        current = move[:2]
        destination = move[2:]

        os.system('cls')
        print(f'Moving {current} to {destination}')
        game.make_move(current, destination)
        game.board.display_layout()
