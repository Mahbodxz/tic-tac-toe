import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def player_move(board):
    while True:
        try:
            move = input("Enter your move (row and column, e.g., 1 2): ").split()
            row, col = int(move[0]) - 1, int(move[1]) - 1
            if (row, col) in get_available_moves(board):
                board[row][col] = "X"
                break
            else:
                print("Invalid move. The cell is either occupied or out of range.")
        except (ValueError, IndexError):
            print("Invalid input. Enter two numbers between 1 and 3 separated by a space.")

def computer_move(board):
    print("Computer is making a move...")
    available_moves = get_available_moves(board)
    row, col = random.choice(available_moves)
    board[row][col] = "O"

def main():
    print("Welcome to Tic-Tac-Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print_board(board)
    
    while True:
        # Player's turn
        player_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if is_full(board):
            print("It's a draw!")
            break

        # Computer's turn
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins! Better luck next time.")
            break
        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()