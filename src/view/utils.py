from model.board import Board
from model.snake import Snake
from model.ladder import Ladder


def dict2board(bdict: dict) -> Board:
    new_board = Board(bdict["size"])
    return new_board


def dict2ladder(ldict: dict) -> Ladder:
    new_ladder = Ladder(ldict["bot"], ldict["top"], ldict["id"])
    return new_ladder


def dict2snake(sdict: dict) -> Snake:
    new_snake = Snake(sdict["head"], sdict["tail"], sdict["id"])
    return new_snake
