from model.ladder import Ladder
from model.snake import Snake


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

    def get_next_pos(self, player_pos: int, steps: int) -> int:
        next_pos = player_pos + steps
        event = "normal"
        if next_pos >= len(self.board):
            return player_pos, "stay"

        try:
            sl_id = self.board[next_pos]
            if sl_id < 0:  # Snake
                idx = self.board.index(sl_id)
                if next_pos > idx:
                    event = "snake"
                return idx, event

            if sl_id > 0:  # Ladder
                idx = self.board.index(sl_id, next_pos + 1)
                if next_pos < idx:
                    event = "ladder"
                return idx, event
        except ValueError:
            return next_pos, event

        return next_pos, event
