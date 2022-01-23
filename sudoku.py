#author: Blake Ballew
import time
accum = 0

def solve_helper(board, indices, curr_index):
    global accum
    while (curr_index < len(indices)):
        accum += 1
        flag = 0
        current_x = (indices[curr_index])[0]
        current_y = (indices[curr_index])[1]
        current_on_board = board[current_x][current_y]

        for x in range(1,10):
            board[current_x][current_y] = x
            if is_valid(board) and x > current_on_board:
                curr_index += 1
                flag = 1
                break

        #no good options -> go back an index
        if flag != 1:
            board[current_x][current_y] = 0
            curr_index -= 1
    return board

def collect_indices(board):
    indices = []
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                indices.append([x,y])
    return indices

def is_valid(board):
    for x in range(9):
        for y in range(9):
            if board[x][y] != 0:
                if not (check_row(board, x, y) and check_column(board, x, y) and check_box(board, x ,y)):
                    return False
    return True

def check_row(board, x, y):
    if board[x].count(board[x][y]) > 1:
        return False
    return True

def check_column(board, x, y):
    for z in range(9):
        if board[z][y] == board[x][y] and z != x:
            return False
    return True

def check_box(board, x, y):
    top_left_x = int(x-(x%3))
    top_left_y = int(y-(y%3))
    for x1 in range(top_left_x,top_left_x+3):
        for y1 in range(top_left_y, top_left_y+3):
            if board[x1][y1] == board[x][y] and x1 != x:
                return False
    return True

def print_board(board):
    for x in range(9):
        for y in range(9):
            print(board[x][y], end = " ")
        print()
    print()

def main(board):
    indices = collect_indices(board)
    solved_puzzle = solve_helper(board, indices, 0)
    print_board(solved_puzzle)


board =  [[7, 0, 5, 6, 2, 0, 8, 0, 0], [0, 2, 0, 8, 0, 9, 0, 7, 5], [3, 0, 8, 7, 4, 5, 0, 2, 1], [5, 3, 0, 2, 0, 6, 0, 1, 0], [0, 0, 2, 0, 0, 0, 5, 0, 0], [0, 7, 0, 5, 0, 4, 0, 6, 2], [2, 5, 0, 0, 6, 7, 0, 8, 4], [0, 8, 0, 4, 5, 2, 0, 9, 0], [0, 0, 7, 0, 0, 0, 2, 5, 0]]



if __name__ == "__main__":
    startTime = time.perf_counter()
    main(board)
    endTime = time.perf_counter()
    print("execution time: ", endTime-startTime)
    print("iterations: ", accum)
