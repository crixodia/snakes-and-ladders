from random import choice


class Dice(object):
    def __init__(self, faces: int = 6):
        """
        Initializes a new Dice instance.

        Args:
            faces (int, optional): The number of faces on the dice. Defaults to 6.
        """
        # seed(0)
        self.faces = faces
        self.dice = [i for i in range(1, faces + 1)]
        self.value = None

    def roll(self) -> int:
        """
        Rolls the dice and returns the result.

        Returns:
            int: The value rolled on the dice.
        """
        self.value = choice(self.dice)
        return self.value

    def __str__(self) -> str:
        """
        Returns a string representation of the dice value.

        Returns:
            str: The string representation of the dice value.
        """
        return str(self.value)
