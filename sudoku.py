#uses a backtracking algorithm to solve boards

def valid(board):
    for row in board:
        for i in row:
            if i != 0 and row.count(i) > 1:
                return False
    cols = get_columns(board)
    for col in cols:
        for j in col:
            if j != 0 and col.count(j) > 1:
                return False
    boxes = get_boxes(board)
    for box in boxes:
        for k in box:
            if k != 0 and box.count(k) > 1:
                return False
    return True

def get_boxes(board):
    boxes = []
    temp = []
    for l in range(0, len(board), 3):
        count = 0
        for row in range(len(board)):
                for col in range(len(board) // 3):
                    temp.append(board[row][col + l])
                count += 1
                if (count == 3) or (count == 6) or (count == 9):
                    boxes.append(temp)
                    temp = []
    return boxes       

def box_num(board, row, col):
    if row in {0, 1, 2} and col in {0, 1, 2}:
        return 0
    elif row in {3, 4, 5} and col in {0, 1, 2}:
        return 1
    elif row in {6, 7, 8} and col in {0, 1, 2}:
        return 2
    elif row in {0, 1, 2} and col in {3, 4, 5}:
        return 3
    elif row in {3, 4, 5} and col in {3, 4, 5}:
        return 4
    elif row in {6, 7, 8} and col in {3, 4, 5}:
        return 5
    elif row in {0, 1, 2} and col in {6, 7, 8}:
        return 6
    elif row in {3, 4, 5} and col in {6, 7, 8}:
        return 7
    elif row in {6, 7, 8} and col in {6, 7, 8}:
        return 8
    else:
        return "WAHT"

def print_board(board):
    [print(*row) for row in board]

def get_columns(board):
    cols = []
    for col in range(len(board)):
        temp = []
        for row in range(len(board)):
            temp.append(board[row][col])
        cols.append(temp)
    return cols

    

def check(board, row, col, value):
    # check row
    for i in board[row]:
        if value == i:
            return False
    # check column
    cols = get_columns(board)
    for j in cols[col]:
        if value == j:
            return False
    # check box
    boxes = get_boxes(board)
    num = box_num(board, row, col)
    for k in boxes[num]:
        if value == k:
            return False

    return True


   


#print(get_boxes(board))
#print(get_columns(board))
#print(box_num(board, 8, 2))
