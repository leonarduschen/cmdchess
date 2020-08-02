import os
from cmdchess.variant import Standard

def main():
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