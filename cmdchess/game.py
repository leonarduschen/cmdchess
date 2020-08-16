"""Game module

"""

import os

from .variant import Standard, MoveException
from .config import configurations


def main(ASCII=True):
    """Run game

    Parameters
    ----------
    ASCII: bool, optional
        Determine whether to run in ASCII or unicode encoding format

    """
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
        while True:
            try:
                if game.to_move == 'W':
                    move = input("White to move: ")
                else:
                    move = input("Black to move: ")
                current = move[:2]
                destination = move[2:]
                game.make_move(current, destination)
            except MoveException:
                print()
            else:
                print(f'Moving {current} to {destination}')
                break

        game.board.display_layout()
