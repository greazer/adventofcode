# %%
%pip install -U numpy
%pip install -U pandas

# %%
from logging.config import valid_ident
import numpy as np
import pprint as pp
import pandas as pd

# %%
with open('Day 7 Input.txt') as fp:
    line = fp.readline()

crab_pos = [int(i, base=10) for i in line.strip().split(',')]
median = int(np.median(crab_pos))

#### median was used for part 1. Isn't really necessary for part 2

# %%

sums_dict = {}
for i in range(1,2000):
    val = 0
    for j in range(1,i):
        val += j
    sums_dict[(i-1)] = val

sums_dict

# %% 

fuel_costs = {}
for target_val in range(0, max(crab_pos)+1):
    fuel = 0
    for i in crab_pos:
        cost = sums_dict[(abs(i-target_val))]
        fuel += cost

    fuel_costs[(target_val)] = fuel

# %%
fuel_costs

# %%
min(fuel_costs.values())
# %%
