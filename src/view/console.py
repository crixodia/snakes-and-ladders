import json
import os

import view.utils as utils
from controller.game import Game
from model.board import Board
from model.ladder import Ladder
from model.snake import Snake
from model.token import Token


class ConsoleView(Game):
    def __init__(self):
        """
        Initializes a new ConsoleView instance.
        """
        players = self.ask_for_players()
        custom_game = input("🤔 Do you want to load a default game? [Y/n] ")

        board = (
            self.load_default_board()
            if custom_game in ["y", "Y"]
            else self.ask_for_board()
        )

        self.game = Game(players, board)
        self.game.start()

        for _ in self.game.play():
            print("-" * 50)
            print(
                f"🎲 {self.game.current_player.name} rolls the dice and get {self.game.dice}"
            )

            if self.game.event == "ladder":
                print(f"🪜  Fortunately {self.game.current_player.name} found a ladder")
            elif self.game.event == "snake":
                print(f"🐍 Unfortunately {self.game.current_player.name} found a snake")
            elif self.game.event == "stay":
                print(f"🥺 {self.game.current_player.name} almost won the game")

            for p in self.game.players:
                print("  ", p)

            input("🔠 Press a key to continue...")

        print(f"🏆 {self.game.winner.name} is the winner.")

    def ask_for_players(self) -> list[Token]:
        """
        Asks the user for the number of players and their names.

        Returns:
            list[Token]: A list of Token instances representing players.
        """
        n_players = int(input("Players count: "))
        players = []
        for i in range(n_players):
            name = input(f"🎮 P{i} name: ")
            players.append(Token(name))
        return players

    def ask_for_board(self) -> Board:
        """
        Asks the user for the board size, number of ladders, and number of snakes.

        Returns:
            Board: The created Board instance.
        """
        b_size = int(input("Board size: "))
        board = Board(b_size)

        n_ladders = int(input("🪜  How many ladders do you want? "))
        n_snakes = int(input("🐍 How many snakes do you want? "))

        for i in range(1, n_ladders + 1):
            top = int(input(f" Bot of the ladder {i}: "))
            bot = int(input(f" Top of the ladder {i}: "))

            l = Ladder(bot, top, i)
            board.add_ladder(l)

        for i in range(1, n_snakes + 1):
            head = int(input(f" Head of the snake {i}: "))
            tail = int(input(f" Tail of the snake {i}: "))

            s = Snake(head, tail, -i)
            board.add_snake(s)

        print("Ladders and snakes will be generated randomly")
        return board

    def load_default_board(self) -> Board:
        """
        Loads the default board configuration from JSON files.

        Returns:
            Board: The created Board instance.
        """
        module_path = os.path.dirname(__file__)
        default_dir = os.path.join(module_path, "default")
        file_names = {
            "board": "board.json",
            "snakes": "snakes.json",
            "ladders": "ladders.json",
        }
        board = Board()

        for fn in file_names:
            file_name = os.path.join(default_dir, file_names.get(fn))
            try:
                with open(file_name) as file:
                    data = json.load(file)
                    if fn == "board":
                        board = utils.dict2board(data)
                    elif fn == "snakes":
                        for snake_data in data:
                            board.add_snake(utils.dict2snake(snake_data))
                    elif fn == "ladders":
                        for ladder_data in data:
                            board.add_ladder(utils.dict2ladder(ladder_data))

            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading {file_name}: {e}")

        return board
