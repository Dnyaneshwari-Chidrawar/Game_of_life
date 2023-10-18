import random
import tkinter
import tkinter as tk


class Game():
    def __init__(self, width, height, cell_size) -> None:
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.board = [[0 for col in range(self.width + 2)] for row in range(self.height + 2)]

    def generate_board(self):
        for row in range(1, self.height + 1):
            for col in range(1, self.width + 1):
                self.board[row][col] = random.randint(0, 1)
        

    def display(self, canvas):
        canvas.delete()
        for row in range(1, self.height + 1):
            for col in range(1, self.width + 1):
                if self.board[row][col] == 1:
                    color = "#57a5ba"
                else:
                    color = 'white'
                sy = row * self.cell_size
                sx = col * self.cell_size
                ex = sx + self.cell_size - 1
                ey = sy + self.cell_size - 1
                canvas.create_rectangle(sx, sy, ex, ey, fill=color, outline='#cad5d9')


    def update_board(self):
        new_board = [[0 for c in range(self.width + 2)] for r in range(self.height + 2)]
        for r in range(1, self.height + 1):
            for c in range(1, self.width + 1):
                sum = (self.board[r - 1][c - 1] + self.board[r - 1][c] + self.board[r - 1][c + 1] +
                       self.board[r][c - 1]     +                        self.board[r][c + 1] +
                       self.board[r + 1][c - 1] + self.board[r + 1][c] + self.board[r + 1][c + 1])
                if sum == 2:
                    new_board[r][c] = self.board[r][c]
                elif sum == 3:
                    new_board[r][c] = 1
        self.board = new_board
        

def run_game_loop(game, delay, root, canvas):
    game.display(canvas)
    game.update_board()
    root.after(delay, lambda : run_game_loop(game, delay, root, canvas))



game = Game(50, 30, 25)
delay = 1
game.generate_board()

root = tk.Tk()
root.title('Game of Life')

canvas = tk.Canvas(root, width=(game.width + 1) * game.cell_size, height=(game.height + 1) * game.cell_size)
canvas.pack()

run_game_loop(game, delay, root, canvas)

root.mainloop()