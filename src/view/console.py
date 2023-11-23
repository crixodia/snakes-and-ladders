from controller.game import Game
from model.board import Board
from model.token import Token


class ConsoleView(Game):
    def __init__(self):
        n_players = int(input("Players count: "))
        players = []
        for i in range(n_players):
            name = input(f"P{i} name: ")
            players.append(Token(name))

        b_size = int(input("Board size: "))
        board = Board(b_size)

        self.game = Game(players, board)
        self.game.start()
        for _ in self.game.play():
            print("-" * 50)
            print(
                f"{self.game.current_player.name} rolls the dice and get {self.game.dice}"
            )

            for p in players:
                print("  ", p)

            input("Press a key to continue...")

        print(f"{self.game.winner.name} is the winner")
