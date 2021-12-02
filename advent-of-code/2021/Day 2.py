# %% [markdown]
# # Setup

# %%
%pip install -U numpy
%pip install -U pandas
import numpy as np
import pandas as pd

# %% [markdown]
# # Read the input file.

# %%
dirs_df = pd.read_csv('Day 2 Input.txt', delimiter=' ')

forward_progress = 0
aim = 0
depth = 0
for index, row in dirs_df.iterrows():
    if (row.direction == 'up'):
        aim -= row.value
    elif (row.direction == 'down'):
        aim += row.value
    else:
        forward_progress += row.value
        depth += aim*row.value
    
print('forward_progress=' + str(forward_progress) + ' ' + 'depth=' + str(depth))
print('answer=' + str(forward_progress * depth))
# %%
