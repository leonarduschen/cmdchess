"""cmdchess

"""
import argparse
from cmdchess.game import main


def play():
    """Entry point

    Run from command-line by invoking cmdchess

    """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-utf",
        "--unicode",
        help="Run with unicode encoding (default encoding is ASCII)",
        action="store_true")
    
    parser.add_argument(
        "-y",
        "--yellow",
        help="Run with yellow board color (default color is cyan)",
        action="store_true")

    args = parser.parse_args()
    if args.unicode:
        encoding = 'UNICODE'
    else:
        encoding = 'ASCII'

    if args.yellow:
        board_color = 'yellow'
    else:
        board_color = 'cyan'

    main(encoding, board_color)
