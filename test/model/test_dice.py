import sys
import unittest
from pathlib import Path
from random import seed

from src.model.dice import Dice

sys.path.append(str(Path(__file__).resolve().parents[2]))


class TestDice(unittest.TestCase):
    def setUp(self):
        # Seed the random number generator for reproducibility
        # Uncomment the line below if you want reproducible results
        seed(0)
        self.dice = Dice()

    # US3 UAT1
    def test_roll_result_between_1_and_faces_inclusive(self):
        for _ in range(1000):  # Repeat the test multiple times for randomness
            self.dice.roll()
            result = self.dice.value
            self.assertTrue(
                1 <= result <= self.dice.faces,
                f"Roll result {result} is not between 1 and {self.dice.faces} inclusive.",
            )


if __name__ == "__main__":
    unittest.main()
