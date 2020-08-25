"""cmdchess

"""
import argparse
from cmdchess.game import main


parser = argparse.ArgumentParser()
parser.add_argument(
    "-utf",
    "--unicode",
    help="Whether console supports unicode encoding",
    action="store_true")
args = parser.parse_args()


def playchess():
    """Run on execution

    """
    if args.unicode:
        main(ASCII=False)
    main()
