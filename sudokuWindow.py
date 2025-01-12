import time
from tkinter import *
from sudoku import *

# board = [[0, 9, 0, 0, 0, 0, 0, 0, 6],
#          [0, 6, 0, 7, 0, 0, 8, 4, 3],
#          [0, 0, 3, 2, 0, 0, 0, 0, 0],
#          [8, 0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 7, 5, 0, 3, 0, 6, 2, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0, 8],
#          [0, 0, 0, 0, 0, 3, 9, 0, 0],
#          [9, 3, 4, 0, 0, 1, 0, 6, 0],
#          [7, 0, 0, 0, 0, 0, 0, 8, 0]]

board = [[0, 0, 0, 6, 8, 0, 0, 0, 0],
         [0, 1, 0, 3, 0, 0, 2, 0, 0],
         [0, 0, 0, 0, 5, 7, 0, 3, 0],
         [2, 0, 0, 0, 0, 0, 9, 0, 7],
         [0, 0, 8, 0, 0, 0, 4, 0, 0],
         [3, 0, 7, 0, 0, 0, 0, 0, 0],
         [9, 0, 0, 0, 0, 6, 7, 0, 0],
         [0, 5, 1, 9, 0, 3, 0, 0, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# board = [[0, 0, 0, 0, 0, 9, 4, 1, 0],
#          [0, 0, 0, 0, 1, 6, 0, 7, 3],
#          [0, 0, 0, 8, 0, 0, 0, 2, 0],
#          [1, 0, 0, 0, 0, 0, 0, 4, 0],
#          [3, 0, 8, 0, 0, 0, 6, 0, 9],
#          [0, 6, 0, 0, 0, 0, 0, 0, 7],
#          [0, 8, 0, 0, 0, 3, 0, 0, 0],
#          [2, 9, 0, 5, 8, 0, 0, 0, 0],
#          [0, 4, 1, 2, 0, 0, 0, 0, 0]] #not too long

# board = [[5, 0, 0, 1, 0, 0, 0, 4, 0],
#          [0, 4, 0, 8, 0, 0, 0, 0, 5],
#          [1, 9, 7, 5, 2, 0, 0, 0, 3],
#          [0, 8, 5, 7, 0, 9, 0, 1, 2],
#          [7, 3, 4, 0, 0, 2, 0, 0, 8],
#          [2, 1, 0, 3, 5, 0, 6, 0, 0],
#          [4, 0, 0, 0, 0, 0, 0, 2, 0],
#          [0, 5, 1, 0, 0, 6, 4, 0, 0],
#          [0, 0, 6, 0, 0, 5, 0, 8, 0]]

#board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
 #        [0, 0, 0, 0, 0, 0, 0, 0, 0],
  #       [0, 0, 0, 0, 0, 0, 0, 0, 0],
   #      [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #     [0, 0, 0, 0, 0, 0, 0, 0, 0],
     #    [0, 0, 0, 0, 0, 0, 0, 0, 0],
      #   [0, 0, 0, 0, 0, 0, 0, 0, 0],
       #  [0, 0, 0, 0, 0, 0, 0, 0, 0],
        # [0, 0, 0, 0, 0, 0, 0, 0, 0]]


window = Tk()
window.title("Sudoku")
canvas = Canvas(height=430, width=408)


window.geometry("500x470")

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
                w = 0.1
                if i == 2 or i == 5:
                        w = 3
                canvas.create_line(x, 25, x, 430, width=w)
                canvas.create_line(3, y, 408, y, width=w)
                x += 45
                y += 45

        canvas.pack()


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
                        updateWindow(canvas, board) #comment this line to disable window

                        if try_solve(board):
                            return True
                        board[row][col] = 0
                return False
    return True   

named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%H:%M:%S", named_tuple)

print("Start time: " + time_string)
bkgBoard(canvas)
try_solve(board)

updateWindow(canvas, board)
window.update() 

named_tuple2 = time.localtime() # get struct_time
time_string2 = time.strftime("%H:%M:%S", named_tuple2)
print("Endtime: " + time_string2)

#add button to start
# try with other boards
#slow it down?
#colored numbers?
#buttons to clear and start program


window.mainloop()