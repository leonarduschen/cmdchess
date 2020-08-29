import pytest
from cmdchess.piece import Piece, King, Queen, Bishop, Knight, Rook, Pawn


class FakePiece(Piece):
    @property
    def notation(self):
        return 'F'

    @property
    def hopping(self):
        return True

    def get_moves(self):
        return []

    def get_captures(self):
        return []


def test_properties():
    piece = FakePiece('W', 'E2')
    assert piece.notation == 'F'
    assert piece.hopping
    assert piece.color == 'W'
    assert piece.position == 'E2'
    piece.position = 'B2'
    assert piece.position == 'B2'


def test_king_properties():
    king = King('B')

    assert king.notation == 'K'
    assert repr(king) == 'BK'
    assert not king.hopping


def test_king_moves_captures():
    king = King('B')

    assert (0, 0) not in king.get_moves()
    assert (-2, -4) not in king.get_moves()
    assert (-2, -2) not in king.get_moves()
    assert (-1, 0) in king.get_moves()
    assert (-1, -1) in king.get_moves()
    assert king.get_moves() == king.get_captures()


def test_queen_properties():
    queen = Queen('W')

    assert queen.notation == 'Q'
    assert repr(queen) == 'WQ'
    assert not queen.hopping


def test_queen_moves_captures():
    queen = Queen('Q')

    assert (0, 0) not in queen.get_moves()
    assert (1, 3) not in queen.get_moves()
    assert (0, 8) not in queen.get_moves()
    assert (7, 0) in queen.get_moves()
    assert (3, 3) in queen.get_moves()
    assert queen.get_moves() == queen.get_captures()


def test_bishop_properties():
    bishop = Bishop('W')

    assert bishop.notation == 'B'
    assert repr(bishop) == 'WB'
    assert not bishop.hopping


def test_bishop_moves_captures():
    bishop = Bishop('W')

    assert (0, 0) not in bishop.get_moves()
    assert (0, 1) not in bishop.get_moves()
    assert (8, 8) not in bishop.get_moves()
    assert (3, -3) in bishop.get_moves()
    assert (-7, -7) in bishop.get_moves()
    assert bishop.get_moves() == bishop.get_captures()


def test_knight_properties():
    knight = Knight('B')

    assert knight.notation == 'N'
    assert repr(knight) == 'BN'
    assert knight.hopping


def test_knight_moves_captures():
    knight = Knight('B')

    assert (0, 0) not in knight.get_moves()
    assert (1, 1) not in knight.get_moves()
    assert (-3, -2) not in knight.get_moves()
    assert (2, 1) in knight.get_moves()
    assert (-1, -2) in knight.get_moves()
    assert knight.get_moves() == knight.get_captures()


def test_rook_properties():
    rook = Rook('B')

    assert rook.notation == 'R'
    assert repr(rook) == 'BR'
    assert not rook.hopping


def test_rook_moves_captures():
    rook = Rook('B')

    assert (0, 0) not in rook.get_moves()
    assert (1, 1) not in rook.get_moves()
    assert (8, 0) not in rook.get_moves()
    assert (4, 0) in rook.get_moves()
    assert (0, 7) in rook.get_moves()
    assert rook.get_moves() == rook.get_captures()


def test_pawn_properties():
    pawn = Pawn('B')

    assert pawn.notation == 'P'
    assert repr(pawn) == 'BP'
    assert not pawn.hopping
    assert pawn.double_advance


def test_pawn_moves_captures():
    pawn_black = Pawn('B')
    pawn_white = Pawn('W')

    assert (0, 0) not in pawn_black.get_moves()
    assert (0, 0) not in pawn_white.get_moves()
    assert (0, -1) in pawn_black.get_moves()
    assert (0, 1) in pawn_white.get_moves()

    # Double advance
    assert (0, -2) in pawn_black.get_moves()
    assert (0, 2) in pawn_white.get_moves()
    pawn_black.double_advance = False
    pawn_white.double_advance = False
    assert (0, -2) not in pawn_black.get_moves()
    assert (0, 2) not in pawn_white.get_moves()

    assert (0, 0) not in pawn_black.get_captures()
    assert (0, 0) not in pawn_white.get_captures()
    assert (-1, -1) in pawn_black.get_captures()
    assert (-1, 1) in pawn_white.get_captures()
    assert (1, -1) in pawn_black.get_captures()
    assert (1, 1) in pawn_white.get_captures()

    assert not any([move in pawn_black.get_captures() for move in pawn_black.get_moves()])
