class TicTacToe:
    def __init__(self, player1, player2):
        self.board = [" " for i in range(9)]  # 3x3 board as a flat list
        self.current_player = player1
        self.other_player = player2

    def print_board(self):
        print()
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print("| " + " | ".join(row) + " |")
        print()

    def play_game(self):
        self.print_board()

        while True:
            move = self.current_player.get_move(self.board)
            self.board[move] = self.current_player.symbol
            self.print_board()

            if self.check_winner(self.current_player.symbol):
                print(f"{self.current_player.name} wins!")
                break
            elif " " not in self.board:
                print("It's a draw!")
                break

            # Switch players
            self.current_player, self.other_player = self.other_player, self.current_player

    def check_winner(self, symbol):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if all(self.board[i] == symbol for i in condition):
                return True
        return False


