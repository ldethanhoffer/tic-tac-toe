import numpy as np
from IPython.display import clear_output
import matplotlib.pyplot as plt


# An additional helper function:
def get_products(board):
    # Compute products accross rows, columns and diagonals:
    row_prod = [np.prod([board[i, j] for i in range(0, 3)]) for j in range(0, 3)]
    col_prod = [np.prod([board[i, j] for j in range(0, 3)]) for i in range(0, 3)]
    diag_prod = [np.prod([board[i, i] for i in range(0, 3)]), np.prod([board[i, 2 - i] for i in range(0, 3)])]
    prods = row_prod + col_prod + diag_prod
    return prods


# The Game class:
class Game:

    def __init__(self):
        self.board = np.matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        self.player = np.random.randint(1, 3)

    def display(self):
        fig, ax = plt.subplots()
        ax.matshow(self.board, cmap='gray')
        for (i, j), z in np.ndenumerate(self.board):
            ax.text(j, i, '{}'.format(z), ha='center', va='center')
        plt.show()

    def evaluate(self):
        prods = get_products(self.board)
        # The current state of the board:
        curr_state = "draw"
        # The possible states of the board:
        states = {1: "player_1 won!", 8: "player_2 won!", 0: "continue"}
        for key in states:
            if key in prods:
                print(states[key])
                curr_state = states[key]
                break
        return curr_state

    def taketurn(self, box):
        # Check whether the chosen box is valid:
        if self.board[box[0], box[1]] != 0:
            print(" you can't use that box:")
        else:
            # replace the box by the player number:
            self.board[box[0], box[1]] = self.player
            # switch players:
            switch = {1: 2, 2: 1}
            self.player = switch[self.player]


# Play the game
def play():
    game = Game()
    print("player {} starts..\n".format(game.player))
    while game.evaluate() == "continue":
        # Get the chosen box:
        print('player {}, choose a box:\n'.format(game.player))
        box = [int(i) for i in input().split()]
        clear_output()
        # take a turn:
        game.taketurn(box)
        # display the resulting board:
        game.display()


# Driver
if __name__ == "__main__":
    play()
