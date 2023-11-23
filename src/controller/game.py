from model.board import Board
from model.dice import Dice
from model.token import Token
from model.snake import Snake
from model.ladder import Ladder


class Game(object):
    def __init__(
        self,
        players: list[Token],
        board: Board,
        snakes: list[Snake] = [],
        ladders: list[Ladder] = [],
        dice: Dice = Dice(6),
    ):
        self.players: list(Token) = players
        self.board: Board = board
        self.dice: Dice = dice

        for s in snakes:
            self.board.add_snake(s)

        for l in ladders:
            self.board.add_ladder(l)

        self.next_player: Token = None
        self.current_player: Token = None
        self.winner: Token = None
        self.event: str = "normal"

    def start(self):
        self.next_player = self.players[0]

    def __move__(self, steps: int):
        if self.winner:
            raise ValueError(
                f"There is already a winner, so it is not possible to move {current_player.name}"
            )

        next_player_pos, e = self.board.get_next_pos(self.next_player.pos, steps)
        self.event = e

        if next_player_pos == self.board.size:
            self.winner = self.next_player

        self.next_player.pos = next_player_pos

    def __next_turn__(self):
        current_player_idx = self.players.index(self.next_player)

        next_player_idx = current_player_idx + 1
        if next_player_idx >= len(self.players):
            next_player_idx = 0

        self.current_player = self.next_player
        self.next_player = self.players[next_player_idx]

    def play(self):
        while not self.winner:
            steps = self.dice.roll()
            self.__move__(steps)
            self.__next_turn__()
            yield
