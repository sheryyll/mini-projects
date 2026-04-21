import tkinter as tk
from tkinter import messagebox

# Game variables
board = [['' for _ in range(3)] for _ in range(3)]
human = 'X'
ai = 'O'
nodes_minimax = 0
nodes_alpha = 0

def check_winner(b):
    for row in b:
        if row[0] == row[1] == row[2] != '':
            return row[0]
    for col in range(3):
        if b[0][col] == b[1][col] == b[2][col] != '':
            return b[0][col]
    if b[0][0] == b[1][1] == b[2][2] != '':
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] != '':
        return b[0][2]
    return None

def is_full(b):
    return all(cell != '' for row in b for cell in row)

# 1. Standard Minimax Algorithm 
def minimax(b, is_max):
    global nodes_minimax
    nodes_minimax += 1

    winner = check_winner(b)
    if winner == ai: return 1
    if winner == human: return -1
    if is_full(b): return 0

    if is_max:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == '':
                    b[i][j] = ai
                    best = max(best, minimax(b, False))
                    b[i][j] = ''
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == '':
                    b[i][j] = human
                    best = min(best, minimax(b, True))
                    b[i][j] = ''
        return best

# 2. Alpha-Beta Pruning Algorithm 
def alphabeta(b, is_max, alpha, beta):
    global nodes_alpha
    nodes_alpha += 1

    winner = check_winner(b)
    if winner == ai: return 1
    if winner == human: return -1
    if is_full(b): return 0

    if is_max:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == '':
                    b[i][j] = ai
                    best = max(best, alphabeta(b, False, alpha, beta))
                    b[i][j] = ''
                    alpha = max(alpha, best)
                    if beta <= alpha: break
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if b[i][j] == '':
                    b[i][j] = human
                    best = min(best, alphabeta(b, True, alpha, beta))
                    b[i][j] = ''
                    beta = min(beta, best)
                    if beta <= alpha: break
        return best

def ai_move():
    global nodes_minimax, nodes_alpha
    best_score = -float('inf')
    move = None

    # Reset counters for the current turn to show comparison
    current_turn_minimax = 0
    current_turn_alpha = 0
    
    # Performance Comparison Logic
    for i in range(3):
        for j in range(3):
            if board[i][j] == '':
                # Run standard minimax to count nodes
                temp_minimax_count = nodes_minimax
                minimax(board, False)
                current_turn_minimax += (nodes_minimax - temp_minimax_count)

                # Run Alpha-Beta to actually determine the move
                temp_alpha_count = nodes_alpha
                board[i][j] = ai
                score = alphabeta(board, False, -float('inf'), float('inf'))
                board[i][j] = ''
                current_turn_alpha += (nodes_alpha - temp_alpha_count)

                if score > best_score:
                    best_score = score
                    move = (i, j)

    if move:
        board[move[0]][move[1]] = ai
        buttons[move[0]][move[1]].config(text=ai, fg="#8A2BE2")
        print(f"Nodes Expanded this turn -> Minimax: {current_turn_minimax}, Alpha-Beta: {current_turn_alpha}")
        
        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Game Over", f"{winner} Wins!")
            root.destroy()
        elif is_full(board):
            messagebox.showinfo("Game Over", "It's a Draw!")
            root.destroy()

def on_click(i, j):
    if board[i][j] == '':
        board[i][j] = human
        buttons[i][j].config(text=human, fg="#DDA0DD")
        
        if not check_winner(board) and not is_full(board):
            ai_move()
        elif check_winner(board):
            messagebox.showinfo("Game Over", "Human Wins!")
            root.destroy()
        elif is_full(board):
            messagebox.showinfo("Game Over", "It's a Draw!")
            root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Tic-Tac-Toe AI ")
root.configure(bg="#F5F5FC")

buttons = [[None]*3 for _ in range(3)]

# Girly Pop Aesthetic Styles
LAVENDER = "#E6E6FA"
LILAC = "#D8BFD8"
DARK_PURPLE = "#4B0082"

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('Verdana', 24, 'bold'),
                                  width=4, height=2,
                                  bg=LAVENDER, activebackground=LILAC,
                                  command=lambda r=i, c=j: on_click(r, c))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

print("--- AI Performance Comparison Started ---")
root.mainloop()