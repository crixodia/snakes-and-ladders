from random import choice, seed


class Dice(object):
    def __init__(self, faces: int = 6):
        #seed(0)
        self.faces = faces
        self.dice = [i for i in range(1, faces + 1)]
        self.value = None

    def roll(self) -> int:
        self.value = choice(self.dice)
        return self.value

    def __str__(self) -> str:
        return str(self.value)
