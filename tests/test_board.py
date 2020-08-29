from cmdchess.board import Square, Board, to_cartesian, to_algebraic
from cmdchess.piece import Rook, Queen


def test_square_properties():
    square = Square('A2', 'light')
    rook = Rook('W')

    assert repr(square) == 'light None A2'
    assert square.position == 'A2'
    assert square.color == 'light'
    assert square.occupant is None
    square.occupant = rook
    assert square.occupant is rook


def test_filter_occupant():
    square = Square('C1', 'dark')
    queen = Queen('B')

    assert square.filter_occupant(color='B') is None
    square.occupant = queen
    assert square.filter_occupant(color='W') is None
    assert square.filter_occupant(color='B') is queen
    assert square.filter_occupant(color='B', notation='Q') is queen


def test_board_properties():
    board = Board()

    keys = [
        'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8',
        'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7',
        'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6',
        'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5',
        'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4',
        'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3',
        'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2',
        'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1',
    ]

    assert all([key in board.keys() for key in keys])


def test_to_cartesian():
    assert to_cartesian('A1') == (1, 1)
    assert to_cartesian('B4') == (2, 4)
    assert to_cartesian('H7') == (8, 7)
    assert to_cartesian('F6') == (6, 6)


def test_to_algebraic():
    assert to_algebraic((1, 1)) == 'A1'
    assert to_algebraic((2, 4)) == 'B4'
    assert to_algebraic((8, 7)) == 'H7'
    assert to_algebraic((6, 6)) == 'F6'
