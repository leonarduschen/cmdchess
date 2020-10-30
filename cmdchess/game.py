"""Game module

"""

import os
from colorama import Back
from .variant import Standard, MoveException
from .config import configurations, UNICODE, ASCII


def clear():
    """Clear command that works on Windows and UNIX systems

    """
    os.system('cls' if os.name == 'nt' else 'clear')


def main(encoding, board_color):
    """Run game

    Parameters
    ----------
    encoding: {'ASCII','UNICODE'}
        Determine whether to run in unicode encoding
    board_color: {'CYAN','YELLOW'}
        Select board color

    """
    if encoding == 'ASCII':
        configurations.symbols = ASCII
    elif encoding == 'UNICODE':
        configurations.symbols = UNICODE

    if board_color == 'cyan':
        configurations.lightsqr = Back.LIGHTCYAN_EX
    elif board_color == 'yellow':
        configurations.lightsqr = Back.YELLOW

    game = Standard()
    while True:
        clear()
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
