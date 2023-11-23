import sys
import unittest
from pathlib import Path

from src.model.board import Board
from src.model.dice import Dice
from src.model.token import Token

sys.path.append(str(Path(__file__).resolve().parents[2]))


class TestToken(unittest.TestCase):
    def setUp(self):
        """
        Set up the test fixture by initializing the Board, Token, and Dice instances.
        """
        self.board = Board()  # Not using snakes and ladders
        self.token = Token("Player")
        self.dice = Dice()

    # US1 UAT1
    def test_token_placed_on_square_1(self):
        """
        Test that the token is initially placed on square 1.

        This test is related to User Story 1, User Acceptance Test 1.
        """
        self.assertEqual(self.token.pos, 1)

    # US1 UAT2
    def test_token_moved_3_spaces(self):
        """
        Test that the token moves 3 spaces forward.

        This test is related to User Story 1, User Acceptance Test 2.
        """
        self.token.next_position(self.board, 3)
        self.assertEqual(self.token.pos, 4)

    # US1 UAT3
    def test_token_moved_3_spaces_and_then_moved_4_spaces(self):
        """
        Test that the token moves 3 spaces and then 4 spaces forward.

        This test is related to User Story 1, User Acceptance Test 3.
        """
        self.token.next_position(self.board, 3)
        self.token.next_position(self.board, 4)
        self.assertEqual(self.token.pos, 8)

    # US2 UAT1
    def test_token_on_square_97_and_moved_3_spaces(self):
        """
        Test that the token, on square 97, moves 3 spaces and wins the game.

        This test is related to User Story 2, User Acceptance Test 1.
        """
        self.token.pos = 97
        self.assertEqual(self.token.next_position(self.board, 3), "win")
        self.assertEqual(self.token.pos, 100)

    # US2 UAT2
    def test_token_on_square_97_and_moved_4_spaces(self):
        """
        Test that the token, on square 97, moves 4 spaces and stays in place.

        This test is related to User Story 2, User Acceptance Test 2.
        """
        self.token.pos = 97
        self.assertEqual(self.token.next_position(self.board, 4), "stay")
        self.assertEqual(self.token.pos, 97)

    # US3 UAT1
    def test_player_rolls_die(self):
        """
        Test that the player rolls the die, and the token moves accordingly.

        This test is related to User Story 3, User Acceptance Test 1.
        """
        result = self.dice.roll()
        last_pos = self.token.pos
        self.token.next_position(self.board, result)
        self.assertEqual(last_pos + result, self.token.pos)


if __name__ == "__main__":
    unittest.main()
