# Rock-Paper-Scissors Game

This is a simple text-based implementation of the classic Rock-Paper-Scissors game in Python. The game allows a user to play against the computer in a series of rounds and keeps track of the score.

## How to Play

1. Clone the repository or download the source code file `rpcGame.py`.
2. Navigate to the directory containing the game files.

## Prerequisites

- Python 3.x 

## Running the Game

1. Open a terminal or command prompt.
2. Navigate to the directory where the game file `rpcGame.py` are located.
3. Run the following command:
`python rock_paper_scissors.py`

4. The game will start, and you'll be prompted to make a choice (1 for Rock, 2 for Paper, 3 for Scissors).
5. After each round, the game will display the user's choice, the computer's choice, the round result, and the updated score.
6. You'll be asked if you want to play another round. Enter 'Y' for yes or 'N' for no.
7. Once you decide to stop playing, the final score will be displayed, and the program will exit.


## Code Structure

- The main game logic is contained in the `rpc_Game()` function.
- `won()` is called when the user wins a round.
- `lose()` is called when the user loses a round.
- `draw()` is called when the round results in a draw.
- The program uses a loop to allow multiple rounds of play until the user decides to quit.
- The user's choice is taken as input, and the computer's choice is randomly generated using the `random` module.


## Author

[@heythakur](https://www.github.com/heythakur)