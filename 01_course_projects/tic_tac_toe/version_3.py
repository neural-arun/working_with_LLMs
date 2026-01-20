import tkinter as tk
from tkinter import messagebox
import random
import sys

# --- Core Game Logic (from previous version, reused) ---

def create_board():
    """
    Initializes a new 3x3 game board.
    The board is a list of 9 elements, representing the 3x3 grid.
    ' ' denotes an empty cell.
    """
    return [' ' for _ in range(9)]

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

# --- AI Opponent Logic (reused with minor changes for GUI) ---

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

# --- Main GUI Application Class ---

class TicTacToeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        
        # Game state variables
        self.board = create_board()
        self.current_player = 'X'
        self.game_active = True
        self.mode = '1-player'
        self.difficulty = 'hard'
        self.ai_player = 'O'
        
        # Scoreboard
        self.scores = {'X_wins': 0, 'O_wins': 0, 'draws': 0}

        # --- UI Elements ---
        
        # Main frames for layout
        self.top_frame = tk.Frame(self.master)
        self.top_frame.pack(pady=10)
        self.grid_frame = tk.Frame(self.master)
        self.grid_frame.pack()
        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.pack(pady=10)

        # Status and score labels
        self.status_label = tk.Label(self.top_frame, text="Player X's turn", font=('Arial', 18))
        self.status_label.pack(side=tk.TOP)
        
        self.score_label = tk.Label(self.top_frame, text="X: 0 | O: 0 | Draws: 0", font=('Arial', 12))
        self.score_label.pack(side=tk.BOTTOM)
        
        # Game board buttons
        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            button = tk.Button(self.grid_frame, text='', font=('Arial', 40), width=3, height=1,
                               command=lambda i=i: self.handle_click(i))
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons.append(button)
            
        # Controls and options
        self.control_frame = tk.Frame(self.bottom_frame)
        self.control_frame.pack()
        
        # Updated style for the New Game button
        self.new_game_button = tk.Button(self.control_frame, text="New Game", command=self.reset_game,
                                         font=('Arial', 14, 'bold'), relief=tk.RAISED, bd=3, padx=10, pady=5)
        self.new_game_button.pack(side=tk.LEFT, padx=10)
        
        # Updated style for difficulty selection
        self.difficulty_var = tk.StringVar(value='hard')
        self.difficulty_menu = tk.OptionMenu(self.control_frame, self.difficulty_var, 'easy', 'medium', 'hard', command=self.set_difficulty)
        self.difficulty_menu.config(font=('Arial', 14, 'bold'), relief=tk.RAISED, bd=3)
        self.difficulty_menu.pack(side=tk.LEFT, padx=10)
        
        # Updated style for game mode selection
        self.mode_var = tk.StringVar(value='1-player')
        self.mode_menu = tk.OptionMenu(self.control_frame, self.mode_var, '1-player', '2-player', command=self.set_mode)
        self.mode_menu.config(font=('Arial', 14, 'bold'), relief=tk.RAISED, bd=3)
        self.mode_menu.pack(side=tk.LEFT, padx=10)
        
        self.start_game()

    def set_difficulty(self, value):
        self.difficulty = value
        
    def set_mode(self, value):
        self.mode = value
        
    def handle_click(self, index):
        """
        Handles a human player's move.
        """
        if self.game_active and is_valid_move(self.board, index):
            self.board[index] = self.current_player
            if self.current_player == 'X':
                self.buttons[index].config(text='✕', fg='red', state=tk.DISABLED)
            else:
                self.buttons[index].config(text='✓', fg='green', state=tk.DISABLED)
            
            self.check_game_state()
            
            if self.game_active:
                self.switch_player()
                if self.mode == '1-player' and self.current_player == self.ai_player:
                    self.master.after(500, self.ai_move)

    def ai_move(self):
        """
        Handles the AI's turn based on the selected difficulty.
        """
        self.status_label.config(text=f"AI ({self.ai_player}) is thinking...")
        self.master.update_idletasks()
        
        if self.difficulty == 'easy':
            move = easy_ai_move(self.board)
        elif self.difficulty == 'medium':
            human_player = 'O' if self.ai_player == 'X' else 'X'
            move = medium_ai_move(self.board, self.ai_player, human_player)
        else: # hard
            human_player = 'O' if self.ai_player == 'X' else 'X'
            move = hard_ai_move(self.board, self.ai_player, human_player)

        if is_valid_move(self.board, move):
            self.board[move] = self.current_player
            if self.current_player == 'X':
                self.buttons[move].config(text='✕', fg='red', state=tk.DISABLED)
            else:
                self.buttons[move].config(text='✓', fg='green', state=tk.DISABLED)
            
            self.check_game_state()
            
            if self.game_active:
                self.switch_player()

    def check_game_state(self):
        """
        Checks for a win or a draw after a move.
        """
        is_win, winning_line = check_win(self.board, self.current_player)
        if is_win:
            self.game_active = False
            self.status_label.config(text=f"Player {self.current_player} wins!")
            self.scores[f'{self.current_player}_wins'] += 1
            self.highlight_winning_line(winning_line)
        elif check_draw(self.board):
            self.game_active = False
            self.status_label.config(text="It's a draw!")
            self.scores['draws'] += 1
            
        if not self.game_active:
            for button in self.buttons:
                button.config(state=tk.DISABLED)
            self.update_score_label()

    def highlight_winning_line(self, indices):
        """
        Changes the background color of the winning buttons.
        """
        for i in indices:
            self.buttons[i].config(bg='lightgreen')
            
    def switch_player(self):
        """
        Switches the current player and updates the status label.
        """
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.config(text=f"Player {self.current_player}'s turn")

    def update_score_label(self):
        self.score_label.config(text=f"X: {self.scores['X_wins']} | O: {self.scores['O_wins']} | Draws: {self.scores['draws']}")

    def start_game(self):
        """
        Sets up the initial game state based on user selection.
        """
        self.board = create_board()
        self.current_player = random.choice(['X', 'O'])
        self.game_active = True
        
        # Randomly assign AI player based on who starts
        if self.mode == '1-player':
            self.ai_player = 'O' if self.current_player == 'X' else 'X'
            self.status_label.config(text=f"Player {self.current_player} starts. You are X.")
            if self.current_player == self.ai_player:
                self.master.after(500, self.ai_move)
        else:
            self.status_label.config(text=f"Player {self.current_player} starts.")
            
        self.update_ui()

    def update_ui(self):
        """
        Resets the visual state of the board.
        """
        for i, button in enumerate(self.buttons):
            button.config(text=self.board[i], state=tk.NORMAL, bg=self.master.cget('bg'), fg='black')
        
    def reset_game(self):
        """
        Resets the entire game state.
        """
        self.board = create_board()
        self.current_player = random.choice(['X', 'O'])
        self.game_active = True
        self.update_ui()
        self.update_score_label()
        
        if self.mode == '1-player':
            self.ai_player = 'O' if self.current_player == 'X' else 'X'
            self.status_label.config(text=f"Player {self.current_player} starts. You are X.")
            if self.current_player == self.ai_player:
                self.master.after(500, self.ai_move)
        else:
            self.status_label.config(text=f"Player {self.current_player} starts.")
        
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
