import tkinter as tk

def populate_board(board):
    global entries
    entries = [[None]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            cell_value = board[i][j]
            if cell_value != 0:
                cell = tk.Label(root, text=str(cell_value), font=('Helvetica', 16, 'bold'), width=4, height=2, bg='lightgrey')
            else:
                entries[i][j] = tk.StringVar()
                cell = tk.Entry(root, textvariable=entries[i][j], font=('Helvetica', 16), width=4)
            cell.grid(row=i, column=j)

def get_input():
    user_input = [[0]*9 for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if entries[i][j] is not None:
                try:
                    value = int(entries[i][j].get())
                    if 1 <= value <= 9:
                        user_input[i][j] = value
                    else:
                        raise ValueError
                except ValueError:
                    tk.messagebox.showerror("Error", "Invalid input. Please enter a number between 1 and 9.")
                    return None
    return user_input

def solve():
    user_input = get_input()
    if user_input:
        # Implement Sudoku solving algorithm here using user_input
        # For simplicity, let's just print the input for now
        print("User input:")
        for row in user_input:
            print(row)

# Example Sudoku board (0 represents empty cells)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")

# Populate the board with Sudoku numbers
populate_board(sudoku_board)

# Button to solve Sudoku
solve_button = tk.Button(root, text="Solve", command=solve)
solve_button.grid(row=10, columnspan=9)

# Run the Tkinter event loop
root.mainloop()
