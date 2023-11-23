import sys
import unittest
from pathlib import Path
from random import seed

from src.model.dice import Dice

sys.path.append(str(Path(__file__).resolve().parents[2]))


class TestDice(unittest.TestCase):
    def setUp(self):
        """
        Set up the test fixture by initializing the Dice instance.
        """
        seed(0)
        self.dice = Dice()

    # US3 UAT1
    def test_roll_result_between_1_and_faces_inclusive(self):
        """
        Test that the result of rolling the dice is between 1 and faces (inclusive).

        This test is related to User Story 3, User Acceptance Test 1.
        """
        for _ in range(1000):  # Repeat the test multiple times for randomness
            self.dice.roll()
            result = self.dice.value
            self.assertTrue(
                1 <= result <= self.dice.faces,
                f"Roll result {result} is not between 1 and {self.dice.faces} inclusive.",
            )


if __name__ == "__main__":
    unittest.main()
