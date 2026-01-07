import math

'''
We'll use:
'X' for the AI
'O' for human
' ' (space) for empty
'''

def print_board(board):
    print()
    for i in range(3):
        row = board[i * 3:(i + 1) * 3]
        print(" " + " | ".join(row))
        if i < 2:
            print("---+---+---")
    print()

def check_winner(board):
    win_combos = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # cols
        (0,4,8), (2,4,6)            # diagonals
    ]

    for a, b, c in win_combos:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]

    return None

def is_board_full(board):
    return all(cell != ' ' for cell in board)

def minimax(board, depth, is_maximizing):
    winner = check_winner(board)

    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                best_score = max(best_score, score)
        return best_score

    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i

    return move

def main():
    while True:  # Loop for replay
        board = [' '] * 9

        print("Welcome to Tic-Tac-Toe!")
        print("You are 'O', and the AI is 'X'.")
        print("Positions are 1-9 like this:")
        print("\n 1 | 2 | 3\n---+---+---\n 4 | 5 | 6\n---+---+---\n 7 | 8 | 9\n")

        # Ensure input is properly taken
        while True:
            human_turn_input = input("Do you want to go first? (y/n): ").strip().lower()
            if human_turn_input in ['y', 'n']:
                break  # Accept the input
            else:
                print("Invalid input. Please enter 'y' or 'n'.")
        
        human_turn = human_turn_input == "y"

        while True:
            print_board(board)

            winner = check_winner(board)
            if winner == 'X':
                print("AI wins!")
                break
            elif winner == 'O':
                print("You win!")
                break
            elif is_board_full(board):
                print("It's a draw!")
                break

            if human_turn:
                while True:
                    try:
                        pos = int(input("Enter your move (1-9): ")) - 1
                        if pos < 0 or pos > 8:
                            print("Invalid position. Choose 1-9.")
                        elif board[pos] != ' ':
                            print("That spot is taken. Try again.")
                        else:
                            board[pos] = 'O'
                            break
                    except ValueError:
                        print("Please enter a number between 1 and 9.")
            else:
                print("AI is thinking...")
                move_index = best_move(board)
                board[move_index] = 'X'

            human_turn = not human_turn

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break  # Exit the loop and end the game

if __name__ == "__main__":
    main()