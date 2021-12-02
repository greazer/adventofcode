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


# %%
forward_progress = sum(dirs_df[(dirs_df.direction=='forward')].value)
ups = sum(dirs_df[(dirs_df.direction=='up')].value)
downs = sum(dirs_df[(dirs_df.direction=='down')].value)

final = forward_progress * (downs - ups)
        

# %%
