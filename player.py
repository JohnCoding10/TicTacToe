import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name} ({self.symbol}), enter your move (1-9): "))
                move-=1
                if move < 0 or move >= 9:
                    print("Invalid input. Please enter a number between 1 and 9.")
                elif board[move] != " ":
                    print("That spot is already taken. Try again.")
                else:
                    return move
            except ValueError:
                print("Please enter a valid number.")


class RandomAI(Player):
    def get_move(self, board):
        available_moves = [i for i, spot in enumerate(board) if spot == " "]
        return random.choice(available_moves)