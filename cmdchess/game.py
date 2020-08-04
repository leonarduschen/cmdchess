import os
import imp


def main():
    import cmdchess.variant
    import cmdchess.displayconfig as displayconfig
    displayconfig.unicode_console.append(True)
    imp.reload(cmdchess.displayconfig)
    imp.reload(cmdchess.variant)
    import cmdchess.variant
    import cmdchess.displayconfig as displayconfig

    game = cmdchess.variant.Standard()
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

if __name__ == '__main__':
    main()
    print()