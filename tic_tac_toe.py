# Tic Tac Toe game where you play against a simple AI

import random

# Board is a list of 9 elements
board = [" " for _ in range(9)]

# Function to print the board
def print_board():
    print("\n")
    for i in range(3):
        print(" | ".join(board[i*3:(i+1)*3]))
        if i != 2:
            print("--+---+--")
    print("\n")

# Function to check for a win
def check_winner(brd, player):
    win_combos = [(0,1,2), (3,4,5), (6,7,8),   # rows
                  (0,3,6), (1,4,7), (2,5,8),   # cols
                  (0,4,8), (2,4,6)]            # diags
    for combo in win_combos:
        if brd[combo[0]] == brd[combo[1]] == brd[combo[2]] == player:
            return True
    return False

# Function to check for draw
def is_draw():
    return " " not in board

# Player's move
def player_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if board[move] == " ":
                board[move] = "X"
                break
            else:
                print("That spot is already taken.")
        except (ValueError, IndexError):
            print("Invalid input. Try a number from 1 to 9.")

# AI move - random strategy
def ai_move():
    available = [i for i in range(9) if board[i] == " "]
    move = random.choice(available)
    board[move] = "O"
    print(f"AI chooses position {move+1}")

# Main game loop
def play_game():
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        player_move()
        print_board()
        if check_winner(board, "X"):
            print("You win! 🎉")
            break
        if is_draw():
            print("It's a draw!")
            break

        ai_move()
        print_board()
        if check_winner(board, "O"):
            print("AI wins! 😢")
            break
        if is_draw():
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    play_game()
