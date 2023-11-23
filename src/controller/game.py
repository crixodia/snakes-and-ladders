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
        """
        Initializes a new Game instance.

        Args:
            players (list[Token]): List of Token instances representing players.
            board (Board): The game board.
            snakes (list[Snake], optional): List of Snake instances on the board.
            ladders (list[Ladder], optional): List of Ladder instances on the board.
            dice (Dice, optional): The dice used in the game. Defaults to a six-sided dice.
        """
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
        """
        Starts the game by setting the initial next player.
        """
        self.next_player = self.players[0]

    def __move__(self, steps: int):
        """
        Moves the current player on the board based on the number of steps rolled.

        Args:
            steps (int): The number of steps to move.

        Raises:
            ValueError: If there is already a winner.
        """
        if self.winner:
            raise ValueError(
                f"There is already a winner, so it is not possible to move {current_player.name}"
            )

        self.event = self.next_player.next_position(self.board, steps)

        if self.event == "win":
            self.winner = self.next_player

    def __next_turn__(self):
        """
        Advances to the next turn, updating the current and next player.
        """
        current_player_idx = self.players.index(self.next_player)

        next_player_idx = current_player_idx + 1
        if next_player_idx >= len(self.players):
            next_player_idx = 0

        self.current_player = self.next_player
        self.next_player = self.players[next_player_idx]

    def play(self):
        """
        Plays the game in a loop until a winner is determined.

        Yields:
            None: Yields control to the caller after each turn.
        """
        while not self.winner:
            steps = self.dice.roll()
            self.__move__(steps)
            self.__next_turn__()
            yield
