# %% [markdown]
# # Setup

# %%
%pip install -U numpy
import numpy as np

# %% [markdown]
# # Read the input file.

# %%
depths = np.loadtxt('Day 1 Input.txt', dtype='int')
depths_len = len(depths)

# %%
increases = 0
decreases = 0

for i, val in enumerate(depths, start=1):
    if (i < depths_len):
        print(str(depths[i-1]) + ', ' + str(depths[i]))
        if (depths[i] != depths[i-1]):
            if (depths[i] > depths[i-1]):
                increases = increases + 1
            else:
                decreases = decreases + 1

print('Increases: ' + str(increases))
print('Decreases: ' + str(decreases))
        
# %%
