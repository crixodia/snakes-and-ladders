from model.board import Board
from model.snake import Snake
from model.ladder import Ladder


def dict2board(bdict: dict) -> Board:
    """
    Converts a dictionary representation of a board to a Board instance.

    Args:
        bdict (dict): Dictionary representation of a board.

    Returns:
        Board: The created Board instance.
    """
    new_board = Board(bdict["size"])
    return new_board


def dict2ladder(ldict: dict) -> Ladder:
    """
    Converts a dictionary representation of a ladder to a Ladder instance.

    Args:
        ldict (dict): Dictionary representation of a ladder.

    Returns:
        Ladder: The created Ladder instance.
    """
    new_ladder = Ladder(ldict["bot"], ldict["top"], ldict["id"])
    return new_ladder


def dict2snake(sdict: dict) -> Snake:
    """
    Converts a dictionary representation of a snake to a Snake instance.

    Args:
        sdict (dict): Dictionary representation of a snake.

    Returns:
        Snake: The created Snake instance.
    """
    new_snake = Snake(sdict["head"], sdict["tail"], sdict["id"])
    return new_snake
