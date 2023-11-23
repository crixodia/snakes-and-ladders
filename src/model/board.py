from .ladder import Ladder
from .snake import Snake


class Board(object):
    def __init__(self, size: int = 100):
        """
        Initializes a new Board instance.

        Args:
            size (int, optional): The size of the board. Defaults to 100.
        """
        self.size = size
        self.board = [0 for _ in range(size + 1)]  # Linear, allows to use any size
        self.snakes = []
        self.ladders = []

    def add_snake(self, snake: Snake):
        """
        Adds a Snake to the board.

        Args:
            snake (Snake): The Snake instance to be added.

        Raises:
            ValueError: If the snake id is not a negative integer less than zero.
        """
        if snake.id >= 0:
            raise ValueError("Snake id must be a negative int less than zero.")

        self.board[snake.head] = snake.id
        self.board[snake.tail] = snake.id
        self.snakes.append(snake)

    def add_ladder(self, ladder: Ladder):
        """
        Adds a Ladder to the board.

        Args:
            ladder (Ladder): The Ladder instance to be added.

        Raises:
            ValueError: If the ladder id is not a positive integer greater than zero.
        """
        if ladder.id <= 0:
            raise ValueError("Ladder id must be a positive int great than zero.")

        self.board[ladder.top] = ladder.id
        self.board[ladder.bot] = ladder.id
        self.ladders.append(ladder)

    def __len__(self) -> int:
        """
        Returns the size of the board.

        Returns:
            int: The size of the board.
        """
        return len(self.board)
