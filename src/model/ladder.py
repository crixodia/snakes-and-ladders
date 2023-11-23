class Ladder(object):
    def __init__(self, bot: int, top: int, id: int):
        """
        Initializes a new Ladder instance.

        Args:
            bot (int): The bottom position of the ladder.
            top (int): The top position of the ladder.
            id (int): The unique identifier for the ladder.
        """
        self.id = id
        self.bot = bot
        self.top = top
