from game import TicTacToe
from player import HumanPlayer, RandomAI

    
def choose_player(name, symbol):
    while True:
        choice = input(f"Choose player type for {name} (human/ai): ").strip().lower()
        if choice == "human":
            return HumanPlayer(name, symbol)
        elif choice == "ai":
            return RandomAI(name, symbol)
        else:
            print("Invalid choice. Please enter 'human' or 'ai'.")

def main():
    print("Welcome to Tic Tac Toe!")

    # Create players
    player1 = HumanPlayer("Player 1", "X")
    player2 = choose_player("Player 2", "O")
    # Or use AI: player2 = RandomAI("Computer", "O")

    # Start game
    game = TicTacToe(player1, player2)
    game.play_game()

if __name__ == "__main__":
    main()

