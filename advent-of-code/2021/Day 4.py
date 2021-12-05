# %% [markdown]
# # Setup

# %%
#%pip install -U numpy
#%pip install -U pandas
#import numpy as np
#import pandas as pd

# %% [markdown]
# # Part 1

# %%
with open('Day 4 Input.txt') as fp:
    choices_list = fp.readline().strip().split(',')

    boards_list = []
    
    line = fp.readline()

    while line:
        board = []
        for i in range(0,5):
            line = fp.readline().strip()
            board.append(np.fromstring(line, int, sep=' '))
        boards_list.append(board)
        line = fp.readline()

        
# %%
def check_for_win(board):
    win = False
    for row in range(0, len(board)):
        row_win = True
        for col in range(0, len(board[row])):
            if board[row][col] != -1:
                row_win = False
                break
        if row_win == True:
            break
    
    for col in range(0, len(board[0])):
        col_win = True
        for row in range(0, len(board)):
            if board[row][col] != -1:
                col_win = False
                break
        if col_win == True:
            break

    return col_win or row_win
# %%            
def mark_choice(val, board):
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if val == board[row][col]:
                board[row][col] = -1

def sum_unmarked(board):
    sum = 0
    for row in range(0, len(board)):
        for col in range(0, len(board[row])):
            if board[row][col] != -1:
                sum += board[row][col]
    return sum

winner_list = []

for i, val in enumerate(choices_list):
    for j, b in enumerate(boards_list):
        if j not in winner_list:
            mark_choice(int(val), b)
            if check_for_win(b):
                winner_list.append(j)
        
    if len(winner_list) == len(boards_list):
        break

last_board_to_win = boards_list[winner_list[len(winner_list)-1]]
sum = sum_unmarked(last_board_to_win)
print(f'Sum Unmarked: {sum}  Value Called: {val}  Answer: {int(val)*sum}')


#%% [markdown]
    if winner == True:
        sum = sum_unmarked(b)
        print(f'Winning board: {j+1}  Sum Unmarked: {sum}  Value Called: {val}  Answer: {int(val)*sum}')
        break


# %%
