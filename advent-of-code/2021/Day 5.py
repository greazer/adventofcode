# %% [markdown]
# # Setup

# %%
#%pip install -U numpy
#%pip install -U pandas
import numpy as np
#import pandas as pd

# %% [markdown]
# # Part 1

# %%
maxdim=1000
valmap_straight = np.zeros((maxdim,maxdim))
valmap_diag = np.zeros((maxdim,maxdim))
# %%
with open('Day 5 Input.txt') as fp:
    line = fp.readline()
    while line:
        coords = line.strip().split('->')
        coords[0] = coords[0].strip()
        coords[1] = coords[1].strip()
        coords[0] = coords[0].split(',')
        coords[1] = coords[1].split(',')
        coords[0] = list(map(int, coords[0]))
        coords[1] = list(map(int, coords[1]))

        start_y = min(coords[0][1], coords[1][1])
        end_y = max(coords[0][1], coords[1][1])

        start_x = min(coords[0][0], coords[1][0])
        end_x = max(coords[0][0], coords[1][0])

        if (start_y == end_y or start_x == end_x):
            for y in range(start_y, end_y+1):
                for x in range(start_x, end_x+1):
                    valmap_straight[y][x] += 1
        else:
            start_y = coords[0][1]
            start_x = coords[0][0]
            y_count = start_y - coords[1][1]
            x_count = start_x - coords[1][0]
            y_dir = -1 if y_count > 0 else 1
            x_dir = -1 if x_count > 0 else 1
            y = start_y
            x = start_x
            num_y = 0
            num_x = 0
            while num_y < abs(y_count) + 1 and num_x < abs(x_count) + 1:
                valmap_diag[y][x] += 1
                y += y_dir
                x += x_dir
                num_y += 1
                num_x += 1

        line = fp.readline()
# %%
overlaps_straight = np.count_nonzero(valmap_straight >= 2)
print(f'overlaps only straight = {overlaps_straight}')
overlaps_diag = np.count_nonzero(valmap_diag >= 2)
print(f'overlaps only diag = {overlaps_diag}')
valmap_combined = valmap_diag + valmap_straight
overlaps_combined = np.count_nonzero(valmap_combined >= 2)
print(f'overlaps combined = {overlaps_combined}')
# %%
