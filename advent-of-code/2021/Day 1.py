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

def count_inc_dec(a):
    incs = 0
    decs = 0
    a_len = len(a)
    for i, val in enumerate(a, start=1):
        if (i < a_len):
            print(str(a[i-1]) + ', ' + str(a[i]))
            if (a[i] != a[i-1]):
                if (a[i] > a[i-1]):
                    incs = incs+ 1
                else:
                    decs = decs + 1
    return incs, decs

increases, decreases = count_inc_dec(depths)

print('Increases: ' + str(increases))
print('Decreases: ' + str(decreases))
        
# %%
# ## Part II
# 3 day window

# %%
# Make new dataset for creating 3 day groups
window = 3
depths_sums = []
for i, val in enumerate(depths, start = window):
    if (i <= depths_len):
        depths_sums.append(sum(depths[i-window:i]))

# %%
increases = 0
decreases = 0

increases, decreases = count_inc_dec(depths_sums)

print('Increases: ' + str(increases))
print('Decreases: ' + str(decreases))


# %%
