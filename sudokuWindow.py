
import time
from tkinter import *
from turtle import clear
from sudoku import *


window = Tk()
window.title("Sudoku")
canvas = Canvas(height=430, width=408)


window.geometry("500x550")

def bkgBoard(canvas):
        #border
        canvas.create_line(3, 25, 3, 430, width=4) #left
        canvas.create_line(3, 430, 408, 430, width=3) #down
        canvas.create_line(3, 25, 408, 25, width=3) #top
        canvas.create_line(408, 25, 408, 430, width=3) # right



        #lines
        x = 48
        y = 70
        for i in range(8):
                w = 1
                if i == 2 or i == 5:
                        w = 3
                canvas.create_line(x, 25, x, 430, width=w)
                canvas.create_line(3, y, 408, y, width=w)
                x += 45
                y += 45

        canvas.pack()



board = [[0, 0, 0, 0, 2, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 3, 0]]


def updateWindow(canvas, board):
        canvas.delete("all")
        bkgBoard(canvas)
        posY = 47.5
        for row in board:
                posX = 25.5
                for cell in row:
                        if cell == 0:
                                cell = " "
                        canvas.create_text(posX, posY, text=cell)
                        posX += 45
                posY += 45
        window.update()
       

def try_solve(board):
    if valid(board) == False:
        return False
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                for value in range(1, len(board)+1): #breaks on third loop
                    if check(board, row, col, value):
                        board[row][col] = value
                        updateWindow(canvas, board)

                        if try_solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True   

bkgBoard(canvas)
try_solve(board)


updateWindow(canvas, board)
window.update()





#add button to start
# try with other boards
#slow it down?
#colored numbers?
#buttons to clear and start program





window.mainloop()