# Snakes and Ladders

Snakes and Ladders is a board game involving two or more players rolling dice to move their tokens across a board. The board is made up of a collection of numbered squares and is adorned with 'snakes' and 'ladders', which link two squares on the board. Snakes link the squares downwards, while ladders link them going upwards. This means that landing at the bottom of a ladder moves you to the top of that ladder, whereas landing on the top of a snake moves you to the bottom of that snake. The objective of the game is to get your token to the final square before your opponents do.

You can find the original challenge [here](instructions.pdf).

- [Snakes and Ladders](#snakes-and-ladders)
  - [How to run the game](#how-to-run-the-game)
  - [How to run the tests](#how-to-run-the-tests)

## How to run the game

The game is written in Python 3.x and requires no external libraries. To run the game, simply run the following command from the root directory of the project:

```bash
python3 ./src/main.py
```

Then the game will ask you to enter the number of players and the number of squares on the board.

```bash
Players count: 2
```

After that, you have to specify wheter you want to use the default snakes and ladders or you want to create your own.

> **Note:** It is recommended to use the default snakes and ladders as the game is not tested with custom snakes and ladders.

```bash
🤔 Do you want to load a default game? [Y/n] 
```

If you choose to create your own, you will be asked to enter the number of snakes and ladders you want to create and then you will be asked to enter the start and end squares of each snake and ladder.

> **Warning:** notice that there is no control over the input, so if you enter a number greater than the number of squares on the board, the game will crash. And be careful not to creater ladders that go down or snakes that go up.

```bash
Board size: 100
🪜  How many ladders do you want? 3
🐍 How many snakes do you want? 3
 Bot of the ladder 1: 0
 Top of the ladder 1: 10
 Bot of the ladder 2: 40
 Top of the ladder 2: 80
 Bot of the ladder 3: 20
 Top of the ladder 3: 99
 Head of the snake 1: 98
 Tail of the snake 1: 1
 Head of the snake 2: 80
 Tail of the snake 2: 50
 Head of the snake 3: 40
 Tail of the snake 3: 10
```

After that, the game will start and you will be asked to press enter to roll the dice.

```bash
🎲 Cristian rolls the dice and get 4
   [5] Cristian
   [1] Gabriel
🔠 Press a key to continue...
```

If someone finds a snake or a ladder, the game will show a message like this:

```bash
🎲 Gabriel rolls the dice and get 6
🪜  Fortunately Gabriel found a ladder
   [12] Cristian
   [26] Gabriel
🔠 Press a key to continue...
```

```bash
🎲 Gabriel rolls the dice and get 4
🐍 Unfortunately Gabriel found a snake
   [45] Cristian
   [11] Gabriel
🔠 Press a key to continue...
```

Whan someone is almost winning but the dice is greater than the number of squares left, the game will show a message like this:

```bash
🎲 Cristian rolls the dice and get 6
🥺 Cristian almost won the game
   [98] Cristian
   [98] Gabriel
🔠 Press a key to continue...
```

When someone wins the game, the game will show a message like this:

```bash
🎲 Gabriel rolls the dice and get 2
   [98] Cristian
   [100] Gabriel
🔠 Press a key to continue...
🏆 Gabriel is the winner.
```

## How to run the tests

The tests are written using the [unittest](https://docs.python.org/3/library/unittest.html) library. To run the tests, simply run the script [`run_tests.py`](./run_test.py) from the root directory of the project.

```bash
python3 ./run_tests.py
```

It will ask you to enter the test engine you want to use. You can choose between `unittest` and `pytest`.

```bash
Choose test engine (unittest/pytest): unittest
```

> **Note:** It is recommended to use `unittest` as unittest no need to install any external libraries. But if you want to use `pytest`, you have to install it first.
>
> ```bash
> pip3 install pytest
> ```
>

Finally, the script will run all the tests and show the results.

```bash
test_roll_result_between_1_and_faces_inclusive (test.model.test_dice.TestDice.test_roll_result_between_1_and_faces_inclusive)
Test that the result of rolling the dice is between 1 and faces (inclusive). ... ok
test_player_rolls_die (test.model.test_token.TestToken.test_player_rolls_die)
Test that the player rolls the die, and the token moves accordingly. ... ok
test_token_moved_3_spaces (test.model.test_token.TestToken.test_token_moved_3_spaces)
Test that the token moves 3 spaces forward. ... ok
test_token_moved_3_spaces_and_then_moved_4_spaces (test.model.test_token.TestToken.test_token_moved_3_spaces_and_then_moved_4_spaces)
Test that the token moves 3 spaces and then 4 spaces forward. ... ok
test_token_on_square_97_and_moved_3_spaces (test.model.test_token.TestToken.test_token_on_square_97_and_moved_3_spaces)
Test that the token, on square 97, moves 3 spaces and wins the game. ... ok
test_token_on_square_97_and_moved_4_spaces (test.model.test_token.TestToken.test_token_on_square_97_and_moved_4_spaces)
Test that the token, on square 97, moves 4 spaces and stays in place. ... ok
test_token_placed_on_square_1 (test.model.test_token.TestToken.test_token_placed_on_square_1)
Test that the token is initially placed on square 1. ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.002s

OK
```

Using `pytest` will show the results like this:

```bash
========================================================================================= test session starts ==========================================================================================
platform win32 -- Python 3.12.0, pytest-7.4.3, pluggy-1.3.0 -- C:\Python312\python.exe
cachedir: .pytest_cache
rootdir: D:\Repositories\snakes-and-ladders
collected 7 items

test/model/test_dice.py::TestDice::test_roll_result_between_1_and_faces_inclusive PASSED                                                                                                          [ 14%]
test/model/test_token.py::TestToken::test_player_rolls_die PASSED                                                                                                                                 [ 28%]
test/model/test_token.py::TestToken::test_token_moved_3_spaces PASSED                                                                                                                             [ 42%]
test/model/test_token.py::TestToken::test_token_moved_3_spaces_and_then_moved_4_spaces PASSED                                                                                                     [ 57%]
test/model/test_token.py::TestToken::test_token_on_square_97_and_moved_3_spaces PASSED                                                                                                            [ 71%]
test/model/test_token.py::TestToken::test_token_on_square_97_and_moved_4_spaces PASSED                                                                                                            [ 85%]
test/model/test_token.py::TestToken::test_token_placed_on_square_1 PASSED                                                                                                                         [100%]

========================================================================================== 7 passed in 0.05s ===========================================================================================
```