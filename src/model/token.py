from .board import Board


class Token(object):
    def __init__(self, name: str):
        """
        Initializes a new Token instance.

        Args:
            name (str): The name of the token.
        """
        self.name = name
        self.pos = 1

    def __str__(self) -> str:
        """
        Returns a string representation of the token.

        Returns:
            str: The string representation of the token.
        """
        return f"[{self.pos}] {self.name}"

    def next_position(self, b: Board, steps: int) -> str:
        """
        Moves the token to the next position based on the number of steps.

        Args:
            b (Board): The game board.
            steps (int): The number of steps to move.

        Returns:
            str: The event that occurred during the move ("normal", "snake", "ladder", "win", or "stay").
        """
        next_pos = self.pos + steps

        if next_pos >= len(b.board):
            return "stay"

        if next_pos == b.size:
            self.pos = b.size
            return "win"

        try:
            sl_id = b.board[next_pos]

            if sl_id < 0:  # Snake
                idx = b.board.index(sl_id)
                event = "snake" if next_pos > idx else "normal"
            elif sl_id > 0:  # Ladder
                idx = b.board.index(sl_id, next_pos + 1)
                event = "ladder" if next_pos < idx else "normal"
            else:
                idx = next_pos
                event = "normal"

            self.pos = idx
            return event

        except ValueError:
            self.pos = next_pos
            return "normal"
