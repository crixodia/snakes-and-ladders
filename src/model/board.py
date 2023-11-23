from .ladder import Ladder
from .snake import Snake


class Board(object):
    def __init__(self, size: int = 100):
        self.size = size
        self.board = [0 for _ in range(size + 1)]  # Linear, allows to use any size
        self.snakes = []
        self.ladders = []

    def add_snake(self, snake: Snake):
        if snake.id >= 0:
            raise ValueError("Snake id must be a negative int less than zero.")

        self.board[snake.head] = snake.id
        self.board[snake.tail] = snake.id
        self.snakes.append(snake)

    def add_ladder(self, ladder: Ladder):
        if ladder.id <= 0:
            raise ValueError("Ladder id must be a positive int great than zero.")

        self.board[ladder.top] = ladder.id
        self.board[ladder.bot] = ladder.id
        self.ladders.append(ladder)

    def __len__(self) -> int:
        return len(self.board)
