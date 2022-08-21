#author: Blake Ballew
#takes as input a 2D list representing a sudoku puzzle
#solves it via the backtracking approach coupled with a while loop
#uses time and a global accumulator variable to display to the user 
#the execution time (that will vary based on the machine) and the number of
#iterations needed to solve the puzzle, which will be a fixed number

import time
accum = 0

def solve_helper(board, indices, curr_index):
    global accum
    length = len(indices)
    while (curr_index < length):
        if (curr_index < 0):
            print("\nError: invalid puzzle")
            break
        
        accum += 1
        flag = 0
        current_x = (indices[curr_index])[0]
        current_y = (indices[curr_index])[1]
        current_on_board = board[current_x][current_y]
        for x in range(1,10):
            board[current_x][current_y] = x
            if is_valid(board, current_x, current_y) and x > current_on_board:
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

def is_valid(board, x, y):
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

def main():
    # board = []
    # print("please enter the puzzle row-by-row, without separation")
    # for x in range(1,10):
    #     print("row", x, ": ", end = "")
    #     row = list(input())
    #     int_map = map(int, row)
    #     to_int = list(int_map)
    #     board.append(to_int)
    # startTime = time.perf_counter()
    # indices = collect_indices(board)
    # solved_puzzle = solve_helper(board, indices, 0)
    # endTime = time.perf_counter()
    # print("\nexecution time: ", endTime-startTime)
    # print("iterations: ", accum)
    # print("puzzle: ")
    # print_board(solved_puzzle)
    board = [[0, 3, 0, 0, 0, 9, 0, 0, 0], [0, 0, 4, 0, 0, 1, 0, 6, 7], [5, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 6, 0, 0, 8, 0, 2, 1], [0, 0, 9, 0, 0, 2, 0, 0, 8], [0, 2, 0, 0, 0, 0, 0, 7, 0], [0, 0, 0, 0, 0, 0, 5, 0, 9], [0, 0, 0, 6, 4, 0, 0, 0, 0], [0, 0, 0, 0, 5, 0, 0, 4, 0]]

    indices = collect_indices(board)
    solved_puzzle = solve_helper(board, indices, 0)
    print_board(solved_puzzle)
    print("iterations: ", accum)

    

if __name__ == "__main__":
    main()
