import sys
import unittest
from pathlib import Path

from src.model.board import Board
from src.model.dice import Dice
from src.model.token import Token

sys.path.append(str(Path(__file__).resolve().parents[2]))


class TestToken(unittest.TestCase):
    def setUp(self):
        self.board = Board()  # Not using snakes and ladders
        self.token = Token("Player")
        self.dice = Dice()

    # US1 UAT1
    def test_token_placed_on_square_1(self):
        self.assertEqual(self.token.pos, 1)

    # US1 UAT2
    def test_token_moved_3_spaces(self):
        self.token.next_position(self.board, 3)
        self.assertEqual(self.token.pos, 4)

    # US1 UAT3
    def test_token_moved_3_spaces_and_then_moved_4_spaces(self):
        self.token.next_position(self.board, 3)
        self.token.next_position(self.board, 4)
        self.assertEqual(self.token.pos, 8)

    # US2 UAT1
    def test_token_on_square_97_and_moved_3_spaces(self):
        self.token.pos = 97
        self.assertEqual(self.token.next_position(self.board, 3), "win")
        self.assertEqual(self.token.pos, 100)

    # US2 UAT2
    def test_token_on_square_97_and_moved_4_spaces(self):
        self.token.pos = 97
        self.assertEqual(self.token.next_position(self.board, 4), "stay")
        self.assertEqual(self.token.pos, 97)

    # US3 UAT1
    def test_player_rolls_die(self):
        result = self.dice.roll()
        last_pos = self.token.pos
        self.token.next_position(self.board, result)
        self.assertEqual(last_pos + result, self.token.pos)


if __name__ == "__main__":
    unittest.main()
