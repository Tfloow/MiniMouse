import tkinter as tk
import numpy as np
import random

def create_maze(size):
    pop = 0.7 # chose between 0 and 1, the highest it is the less wall there is

    random.seed()
    maze = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            val = random.random()
            if val > pop :
                maze[i][j] = 1

    # The target
    place = random.randint(0, size*size)
    maze[place%size][place//size] = 2

    if(place == 0):
        maze[size][size] = 3
    else:
        maze[0][0] = 3

    return maze

def good_maze():
    maze = [[3, 0, 0, 0, 0, 1, 1, 1, 0, 0,],
            [1, 1, 1, 1, 0, 1, 0, 0, 0, 1,],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1,],
            [1, 1, 1, 1, 1, 0, 1, 0, 0, 0,],
            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0,],
            [2, 1, 0, 1, 0, 1, 0, 1, 1, 1,],
            [1, 1, 0, 0, 0, 1, 0, 1, 0, 1,],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0,],
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 1,],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0,]]
    return maze

def small_good_maze():
    maze= [[3, 0, 0],
           [1, 1, 0],
           [2, 0, 0]]
    return maze

def write_around(maze, x, y, val, span):
    size = len(maze)
    
    # Top of the square
    if(x-span < 0):
        print("not needed")
        pass
    else:
        for i in range(-span, span+1):
            if (i+y < 0) or (i+y >= size):
                print("nope")
                pass 
            else:
                maze[x-span][y+i] = val
    
    # The middle
    for i in range(-span+1, span):
        print(i)
        for j in range(-1, 2, 2):
            if(x + i < 0) or (x + i >= size) or (y + j*span <0) or (y + j*span >= size):
                continue
            else:
                maze[x + i][y + j*span] = val
    
    # Bottom of the square
    if(x+span >= size):
        print("not needed")
        pass
    else:
        for i in range(-span, span+1):
            if (i+y < 0) or (i+y >= size):
                print("nope")
                pass 
            else:
                maze[x+span][y+i] = val
        
    
    print(maze)
    return maze

def solve_maze(maze):

    # Find the starting point
    for i,line in enumerate(maze):
        line = np.array(line)
        if len(np.where(line == 3)[0]) == 1:
            start_pos = (i, np.where(line == 3)[0][0])
            break 

    print(start_pos)

    return 0

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
    #window()
    print(np.array(write_around(good_maze(), 5, 5, 10, 2)))
