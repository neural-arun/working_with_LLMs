import random
import sys

# --- Game Board and Core Logic ---

def create_board():
    """
    Initializes a new 3x3 game board.
    The board is a list of 9 elements, representing the 3x3 grid.
    ' ' denotes an empty cell.
    """
    return [' ' for _ in range(9)]

def print_board(board):
    """
    Prints the current state of the game board in a 3x3 grid format.
    Uses separators to make the grid visually clear.
    """
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')

def check_win(board, player):
    """
    Checks if the specified player has won the game.
    A win is achieved by getting three of their marks in a row, column, or diagonal.
    Returns a tuple: (True if win, winning_line_indices).
    """
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]            # Diagonals
    ]
    for condition in winning_conditions:
        if all(board[i] == player for i in condition):
            return True, condition
    return False, None

def check_draw(board):
    """
    Checks if the game has ended in a draw.
    A draw occurs if there are no more empty cells and no player has won.
    """
    return ' ' not in board

def is_valid_move(board, move):
    """
    Checks if a chosen move is valid.
    A move is valid if the cell index is within the board range and the cell is empty.
    """
    return 0 <= move < 9 and board[move] == ' '

# --- AI Opponent Logic ---

def easy_ai_move(board):
    """
    AI difficulty: Easy.
    Selects a random legal move from all available empty cells.
    """
    empty_cells = [i for i, cell in enumerate(board) if cell == ' ']
    return random.choice(empty_cells)

def medium_ai_move(board, ai_player, human_player):
    """
    AI difficulty: Medium.
    Uses a rule-based heuristic approach to choose the best move.
    1. Win if possible.
    2. Block the opponent's winning move.
    3. Take the center (position 4).
    4. Take a corner (0, 2, 6, 8).
    5. Take a side (1, 3, 5, 7).
    """
    # Check for a winning move for the AI
    for i in range(9):
        if is_valid_move(board, i):
            board_copy = list(board)
            board_copy[i] = ai_player
            if check_win(board_copy, ai_player)[0]:
                return i

    # Check to block the opponent's winning move
    for i in range(9):
        if is_valid_move(board, i):
            board_copy = list(board)
            board_copy[i] = human_player
            if check_win(board_copy, human_player)[0]:
                return i

    # Prioritize center, corners, then sides
    center = 4
    corners = [0, 2, 6, 8]
    sides = [1, 3, 5, 7]

    if is_valid_move(board, center):
        return center
    
    available_corners = [i for i in corners if is_valid_move(board, i)]
    if available_corners:
        return random.choice(available_corners)

    available_sides = [i for i in sides if is_valid_move(board, i)]
    if available_sides:
        return random.choice(available_sides)

    # Fallback to random move if no strategic moves are available
    return easy_ai_move(board)


# --- Minimax Algorithm for Hard AI ---

def minimax(board, depth, is_maximizing, ai_player, human_player):
    """
    The Minimax algorithm to find the optimal move for the AI.
    It assumes both players play optimally.
    - `board`: current game state.
    - `depth`: current depth in the game tree.
    - `is_maximizing`: True if it's the AI's turn to maximize the score.
    - `ai_player`: 'X' or 'O' for the AI.
    - `human_player`: 'X' or 'O' for the human.
    """
    # Check for terminal states (win, lose, draw)
    if check_win(board, ai_player)[0]:
        return 10 - depth
    if check_win(board, human_player)[0]:
        return depth - 10
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -sys.maxsize
        for i in range(9):
            if is_valid_move(board, i):
                board[i] = ai_player
                score = minimax(board, depth + 1, False, ai_player, human_player)
                board[i] = ' '  # Undo the move
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = sys.maxsize
        for i in range(9):
            if is_valid_move(board, i):
                board[i] = human_player
                score = minimax(board, depth + 1, True, ai_player, human_player)
                board[i] = ' '  # Undo the move
                best_score = min(score, best_score)
        return best_score

def hard_ai_move(board, ai_player, human_player):
    """
    AI difficulty: Hard/Unbeatable.
    Uses the Minimax algorithm to find the best possible move.
    """
    best_move = -1
    best_score = -sys.maxsize
    
    for i in range(9):
        if is_valid_move(board, i):
            board[i] = ai_player
            score = minimax(board, 0, False, ai_player, human_player)
            board[i] = ' '  # Undo the move
            
            if score > best_score:
                best_score = score
                best_move = i
    return best_move

# --- Main Game Loop and UI ---

def get_player_choice(board, player):
    """
    Prompts the human player for their move and validates it.
    Repeats until a valid move is entered.
    """
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if is_valid_move(board, move):
                return move
            else:
                print("Invalid move. That cell is already taken or out of range. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def get_ai_difficulty():
    """
    Asks the user to select the AI difficulty level.
    """
    while True:
        choice = input("Select AI difficulty (easy, medium, hard): ").lower().strip()
        if choice in ['easy', 'medium', 'hard']:
            return choice
        else:
            print("Invalid choice. Please choose from easy, medium, or hard.")

def get_game_mode():
    """
    Asks the user to select the game mode.
    """
    while True:
        choice = input("Select game mode (1-player vs AI, 2-player local): ").lower().strip()
        if choice in ['1-player', '2-player']:
            return choice
        else:
            print("Invalid choice. Please choose from 1-player or 2-player.")

def play_game():
    """
    Main function to run the Tic-Tac-Toe game.
    Manages the game state, turns, and game modes.
    """
    scores = {'X_wins': 0, 'O_wins': 0, 'draws': 0}
    
    while True:
        board = create_board()
        players = ['X', 'O']
        current_player = random.choice(players)  # Randomly choose who starts
        
        print("\n--- Tic-Tac-Toe ---")
        print(f"Player {current_player} goes first.")
        
        mode = get_game_mode()
        if mode == '1-player':
            difficulty = get_ai_difficulty()
            ai_player = 'O' if current_player == 'X' else 'X'
            print(f"You are player {'X' if current_player == 'X' else 'O'}. You will play against a {difficulty} AI.")
            
        
        while True:
            print_board(board)
            
            if mode == '2-player' or current_player != ai_player:
                move = get_player_choice(board, current_player)
                board[move] = current_player
            else: # AI's turn
                print(f"AI ({current_player}) is thinking...")
                if difficulty == 'easy':
                    move = easy_ai_move(board)
                elif difficulty == 'medium':
                    move = medium_ai_move(board, ai_player, 'O' if ai_player == 'X' else 'X')
                else: # hard
                    move = hard_ai_move(board, ai_player, 'O' if ai_player == 'X' else 'X')
                board[move] = current_player
                print(f"AI plays at position {move + 1}")

            is_win, winning_line = check_win(board, current_player)
            if is_win:
                print_board(board)
                print(f"\nPlayer {current_player} wins!")
                if current_player == 'X':
                    scores['X_wins'] += 1
                else:
                    scores['O_wins'] += 1
                break
            
            if check_draw(board):
                print_board(board)
                print("\nIt's a draw!")
                scores['draws'] += 1
                break
            
            # Switch turns
            current_player = 'O' if current_player == 'X' else 'X'
            
        print("\n--- Scoreboard ---")
        print(f"X wins: {scores['X_wins']}")
        print(f"O wins: {scores['O_wins']}")
        print(f"Draws: {scores['draws']}")
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    play_game()
