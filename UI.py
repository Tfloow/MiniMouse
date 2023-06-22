import tkinter as tk
from Solver import *

def draw():
    testing = tk.Canvas()
    size=10
    maze = good_maze() #create_maze(size)

    testing.create_rectangle(10, 10, 10+10*size, 10+10*size)

    for i in range(size):
        for j in range(size):
            if(maze[i][j] >= 1):
                color="black"
                if(maze[i][j] == 2):
                    color="red"
                if(maze[i][j] == 3):
                    color="green"
                testing.create_rectangle(10+j*10, 10+i*10, 20+j*10, 20+i*10, fill=color)

    testing.pack(fill=tk.BOTH, expand=1)

def window():
    root = tk.Tk()
    root.title("maze")
    root.config(bg="white")
    root.maxsize(1920,1080)
    root.minsize(300,300)

    draw()

    root.mainloop()
    
if __name__ == '__main__':
    window()