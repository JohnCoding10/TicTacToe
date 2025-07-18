from game import TicTacToe
from player import HumanPlayer, RandomAI

    
def choose_player(name, symbol):
    #Allows the option to play with an AI or human
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

    player1 = HumanPlayer("Player 1", "X")
    player2 = choose_player("Player 2", "O")

    # Track who starts first
    first_player, second_player = player1, player2

    while True:
        # Start a new game with the current first player
        game = TicTacToe(first_player, second_player)
        game.play_game()

        # Ask if they want to play again
        again = input("Play again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing!")
            break

        # Flips who goes first
        first_player, second_player = second_player, first_player


if __name__ == "__main__":
    main()

