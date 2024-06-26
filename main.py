def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the current player has won."""
    # Check rows, columns and diagonals
    win_conditions = [
        # Rows
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Columns
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonals
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]]
    ]
    return [player, player, player] in win_conditions

def check_draw(board):
    """Check if the game is a draw."""
    for row in board:
        if " " in row:
            return False
    return True

def get_move(board):
    """Get a valid move from the current player."""
    while True:
        move = input("Enter your move (row and column): ").split()
        if len(move) != 2:
            print("Please enter two numbers for row and column.")
            continue
        
        row, col = move
        if not (row.isdigit() and col.isdigit()):
            print("Please enter valid numbers for row and column.")
            continue
        
        row, col = int(row) - 1, int(col) - 1
        if row not in range(3) or col not in range(3):
            print("Please enter numbers between 1 and 3 for row and column.")
            continue
        
        if board[row][col] != " ":
            print("That position is already taken. Please choose another.")
            continue
        
        return row, col

def main():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        row, col = get_move(board)
        board[row][col] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
