# %% [markdown]
# # Setup

# %%
#%pip install -U numpy
#%pip install -U pandas
import numpy as np
import pprint as pp
#import pandas as pd

# %% [markdown]
# # Part 1

# %%
fish_list = []
with open('Day 6 Input Test.txt') as fp:
    line = fp.readline()

temp_list = line.strip().split(',')
fish_list = [int(i, base=10) for i in temp_list]

num_days = 18

def calc_num_fish(days):
    for day in range(0,num_days):
        new_fish_index = len(fish_list)
        for i, fish_timer in enumerate(fish_list):
            if i < new_fish_index:
                if fish_timer == 0:
                    fish_list[i] = 6
                    fish_list.append(8)
                else:
                    fish_list[i] -= 1
    return len(fish_list)

pp.pprint(f'{calc_num_fish(num_days)} fish')

# %%
print(f'total fish after {num_days} = {len(fish_list)}')

##########################################################
# %% [markdown]
# # Part 2        
        
# %%
fish_list = []
with open('Day 6 Input Test.txt') as fp:
    line = fp.readline()

temp_list = line.strip().split(',')
fish_list = np.array([int(i, base=10) for i in temp_list])

fish_counts = np.zeros((8))
fish_set = set(fish_list)
for fish_idx in fish_set:
    for i in fish_list:
        if (i == fish_idx):
            fish_counts[fish_idx] += 1

print(np.sum(fish_counts))

#%%
def count_of(list, val):
    c = 0
    for i in list:
        if list[i] == val:
            c +=1
    return c
#[0, 1, 1, 2, 1, 0, 0, 0])

new_fish_counts = np.zeros((8))
add_new = False
for day in range(0, num_days):
    add_new = False
    for i in range(0, len(fish_counts)):
        if i == 0 and fish_counts[i] > 0:
            add_new = True
            new_fish_counts[0] = 0
        elif i > 0:
            new_fish_counts[i-1] = fish_counts[i]
            if i == 7:
                new_fish_counts[7] = 0

    if add_new:    
        new_fish_counts[7] += fish_counts[0]
        new_fish_counts[6] += fish_counts[0]

    fish_counts = np.copy(new_fish_counts)


print(sum(fish_counts))

##############################################


#%%
# CHEAT
with open("Day 6 Input.txt", "r", encoding="utf-8") as ifile:
    livestock = list(map(int, ifile.read().split(",")))


class Cycle:
    def __init__(self, initial, cycles):
        self.cycles = cycles
        self.old_timers = {val: initial.count(val) for val in set(initial)}
        self.cycle_timers()
        print("Nr of fish after {} cycles: {}".format(self.cycles, sum(self.old_timers[val] for val in self.old_timers)))

    def cycle_timers(self):
        for cycles in range(self.cycles-1):
            new_timers = {timer_value-1: self.old_timers.get(timer_value, 0) for timer_value in range(1, 9)}
            if 0 in self.old_timers:
                newly_bred = self.old_timers[0]
                new_timers[8] = newly_bred
                new_timers[6] = new_timers.get(6, 0)+newly_bred
            self.old_timers = new_timers


lf = Cycle(livestock, 80)
lf = Cycle(livestock, 256)
