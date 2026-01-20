import tkinter as tk
from tkinter import messagebox
import random
import sys

# --- Core Game Logic ---
def create_board():
    return [' ' for _ in range(9)]

def check_win(board, player):
    winning_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for condition in winning_conditions:
        if all(board[i] == player for i in condition):
            return True, condition
    return False, None

def check_draw(board):
    return ' ' not in board

def is_valid_move(board, move):
    return 0 <= move < 9 and board[move] == ' '

# --- AI Opponent Logic ---
def easy_ai_move(board):
    return random.choice([i for i, cell in enumerate(board) if cell == ' '])

def medium_ai_move(board, ai_player, human_player):
    for i in range(9):
        if is_valid_move(board, i):
            board_copy = list(board)
            board_copy[i] = ai_player
            if check_win(board_copy, ai_player)[0]:
                return i
    for i in range(9):
        if is_valid_move(board, i):
            board_copy = list(board)
            board_copy[i] = human_player
            if check_win(board_copy, human_player):
                return i
    if is_valid_move(board, 4): return 4
    for corner in [0, 2, 6, 8]:
        if is_valid_move(board, corner): return corner
    for side in [1, 3, 5, 7]:
        if is_valid_move(board, side): return side
    return easy_ai_move(board)

def minimax(board, depth, is_maximizing, ai_player, human_player):
    if check_win(board, ai_player): return 10 - depth
    if check_win(board, human_player): return depth - 10
    if check_draw(board): return 0
    if is_maximizing:
        best_score = -sys.maxsize
        for i in range(9):
            if is_valid_move(board, i):
                board[i] = ai_player
                score = minimax(board, depth + 1, False, ai_player, human_player)
                board[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = sys.maxsize
        for i in range(9):
            if is_valid_move(board, i):
                board[i] = human_player
                score = minimax(board, depth + 1, True, ai_player, human_player)
                board[i] = ' '
                best_score = min(score, best_score)
        return best_score

def hard_ai_move(board, ai_player, human_player):
    best_move, best_score = -1, -sys.maxsize
    for i in range(9):
        if is_valid_move(board, i):
            board[i] = ai_player
            score = minimax(board, 0, False, ai_player, human_player)
            board[i] = ' '
            if score > best_score:
                best_score, best_move = score, i
    return best_move

# --- GUI Application ---
class TicTacToeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("✨ Tic-Tac-Toe ✨")
        self.master.configure(bg="#1e1e2e")

        self.board = create_board()
        self.current_player = 'X'
        self.game_active = True
        self.mode = '1-player'
        self.difficulty = 'hard'
        self.ai_player = 'O'
        self.scores = {'X_wins': 0, 'O_wins': 0, 'draws': 0}

        self.top_frame = tk.Frame(self.master, bg="#1e1e2e")
        self.top_frame.pack(pady=15)
        self.grid_frame = tk.Frame(self.master, bg="#1e1e2e")
        self.grid_frame.pack()
        self.bottom_frame = tk.Frame(self.master, bg="#1e1e2e")
        self.bottom_frame.pack(pady=10)

        self.status_label = tk.Label(self.top_frame, text="Player X's turn", 
                                     font=('Arial', 20, 'bold'), bg="#1e1e2e", fg="#f2f2f2")
        self.status_label.pack()
        self.score_label = tk.Label(self.top_frame, text="X: 0 | O: 0 | Draws: 0", 
                                    font=('Arial', 14), bg="#1e1e2e", fg="#a1a1a1")
        self.score_label.pack()

        # Game buttons styled prettily
        self.buttons = []
        for i in range(9):
            row, col = divmod(i, 3)
            button = tk.Button(self.grid_frame, text='', font=('Arial', 36, 'bold'),
                               width=3, height=1, relief="raised", bd=5,
                               bg="#2f2f3f", fg="white", activebackground="#444", 
                               cursor="hand2", command=lambda i=i: self.handle_click(i))
            button.grid(row=row, column=col, padx=8, pady=8)
            self.buttons.append(button)

        self.control_frame = tk.Frame(self.bottom_frame, bg="#1e1e2e")
        self.control_frame.pack()

        self.new_game_button = tk.Button(self.control_frame, text="🔄 New Game", 
                                         command=self.reset_game, font=('Arial', 14, 'bold'),
                                         relief="raised", bd=4, bg="#ff9800", fg="white",
                                         activebackground="#ffa733", padx=10, pady=5, cursor="hand2")
        self.new_game_button.pack(side=tk.LEFT, padx=10)

        self.difficulty_var = tk.StringVar(value='hard')
        self.difficulty_menu = tk.OptionMenu(self.control_frame, self.difficulty_var,
                                             'easy', 'medium', 'hard', self.set_difficulty)
        self.difficulty_menu.config(font=('Arial', 14, 'bold'), bg="#607d8b", fg="white", bd=0,
                                    activebackground="#78909c", cursor="hand2")
        self.difficulty_menu.pack(side=tk.LEFT, padx=10)

        self.mode_var = tk.StringVar(value='1-player')
        self.mode_menu = tk.OptionMenu(self.control_frame, self.mode_var, '1-player', '2-player', self.set_mode)
        self.mode_menu.config(font=('Arial', 14, 'bold'), bg="#4caf50", fg="white", bd=0,
                              activebackground="#66bb6a", cursor="hand2")
        self.mode_menu.pack(side=tk.LEFT, padx=10)
        
        self.start_game()

    def set_difficulty(self, value): self.difficulty = value
    def set_mode(self, value): self.mode = value

    def handle_click(self, index):
        if self.game_active and is_valid_move(self.board, index):
            self.board[index] = self.current_player
            self.update_button(index)
            self.check_game_state()
            if self.game_active:
                self.switch_player()
                if self.mode == '1-player' and self.current_player == self.ai_player:
                    self.master.after(500, self.ai_move)

    def ai_move(self):
        self.status_label.config(text="🤖 AI is thinking...")
        self.master.update_idletasks()
        human_player = 'O' if self.ai_player == 'X' else 'X'
        move = (easy_ai_move(self.board) if self.difficulty == 'easy' else
                medium_ai_move(self.board, self.ai_player, human_player) if self.difficulty == 'medium'
                else hard_ai_move(self.board, self.ai_player, human_player))
        if is_valid_move(self.board, move):
            self.board[move] = self.current_player
            self.update_button(move)
            self.check_game_state()
            if self.game_active: self.switch_player()

    def update_button(self, index):
        text, color = ('✕', "#e91e63") if self.current_player == 'X' else ('◯', "#00e676")
        self.buttons[index].config(text=text, fg=color, state=tk.DISABLED, disabledforeground=color)

    def check_game_state(self):
        is_win, winning_line = check_win(self.board, self.current_player)
        if is_win:
            self.game_active = False
            self.status_label.config(text=f"⭐ Player {self.current_player} Wins! ⭐", fg="#ffeb3b")
            self.scores[f'{self.current_player}_wins'] += 1
            self.highlight_winning_line(winning_line)
        elif check_draw(self.board):
            self.game_active = False
            self.status_label.config(text="It's a Draw!", fg="#ff5722")
            self.scores['draws'] += 1
        if not self.game_active:
            for b in self.buttons: b.config(state=tk.DISABLED)
            self.update_score_label()

    def highlight_winning_line(self, indices):
        for i in indices:
            self.buttons[i].config(bg="#81c784")

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
        self.status_label.config(text=f"Player {self.current_player}'s turn", fg="#f2f2f2")

    def update_score_label(self):
        self.score_label.config(text=f"X: {self.scores['X_wins']} | O: {self.scores['O_wins']} | Draws: {self.scores['draws']}")

    def start_game(self):
        self.board = create_board()
        self.current_player = random.choice(['X', 'O'])
        self.game_active, self.ai_player = True, ('O' if self.current_player == 'X' else 'X')
        if self.mode == '1-player':
            self.status_label.config(text=f"Player {self.current_player} starts. You are X.", fg="#f2f2f2")
            if self.current_player == self.ai_player:
                self.master.after(500, self.ai_move)
        else:
            self.status_label.config(text=f"Player {self.current_player} starts.", fg="#f2f2f2")
        self.update_ui()

    def update_ui(self):
        for i, button in enumerate(self.buttons):
            if self.board[i] == 'X':
                button.config(text='✕', fg="#e91e63", bg="#2f2f3f", state=tk.DISABLED)
            elif self.board[i] == 'O':
                button.config(text='◯', fg="#00e676", bg="#2f2f3f", state=tk.DISABLED)
            else:
                button.config(text='', state=tk.NORMAL, bg="#2f2f3f")

    def reset_game(self):
        self.board, self.current_player, self.game_active = create_board(), random.choice(['X', 'O']), True
        self.update_ui(); self.update_score_label()
        if self.mode == '1-player':
            self.ai_player = 'O' if self.current_player == 'X' else 'X'
            self.status_label.config(text=f"Player {self.current_player} starts. You are X.", fg="#f2f2f2")
            if self.current_player == self.ai_player: self.master.after(500, self.ai_move)
        else:
            self.status_label.config(text=f"Player {self.current_player} starts.", fg="#f2f2f2")

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToeGame(root)
    root.mainloop()
