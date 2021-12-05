# %% [markdown]
# # Setup

# %%
%pip install -U numpy
%pip install -U pandas
from turtle import heading
import numpy as np
import pandas as pd

# %% [markdown]
# # Part 1

# %%
bin_input = pd.read_csv('Day 3 Input.txt', dtype='str')

# %%
gamma = ''
epsilon = ''
for bit_pos in range(0,len(bin_input.value[0])):
    count_ones = 0
    count_zeros = 0
    for i, row in bin_input.iterrows():
        if (row.value[bit_pos] == '1'):
            count_ones += 1
        else:
            count_zeros += 1      

    if count_ones > count_zeros:
        gamma += '1'
        epsilon += '0'
    elif count_ones < count_zeros:
        gamma += '0'
        epsilon += '1'
        
print(f'gamma: {gamma}, epsilon {epsilon}), answer: {int(epsilon,2) * int(gamma,2)}')

# %% [markdown]
# # Part 2

# %%
def count_digits(list_df, pos):
    count_ones = 0
    count_zeros = 0
    for i, row in list_df.iterrows():
        if (row.value[pos] == '1'):
            count_ones += 1
        else:
            count_zeros += 1    
    return count_zeros, count_ones  

# %%
oxy_list = bin_input
scrubber_list = bin_input
oxy_val = ''
scrubber_val = ''
overall_bit_pos = 0

for overall_bit_pos in range(0, len(bin_input.value[0])):
    count_zeros, count_ones = count_digits(oxy_list, overall_bit_pos)
    new_oxy_val = '1'
    if (count_ones < count_zeros):
        new_oxy_val = '0'

    if oxy_list.shape[0] > 1:       
        oxy_list = oxy_list[oxy_list['value'].str[overall_bit_pos] == new_oxy_val]
    
    if oxy_list.shape[0] == 1:
        oxy_val = oxy_list.iat[0,0]

    count_zeros, count_ones = count_digits(scrubber_list, overall_bit_pos)
    new_scrubber_val = '0'
    if (count_ones < count_zeros):
        new_scrubber_val = '1'

    if scrubber_list.shape[0] > 1:       
        scrubber_list = scrubber_list[scrubber_list['value'].str[overall_bit_pos] == new_scrubber_val]

    if scrubber_list.shape[0] == 1:
        scrubber_val = scrubber_list.iat[0,0]

    overall_bit_pos += 1

print(oxy_val)
print(scrubber_val)
print(int(oxy_val,2) * int(scrubber_val,2))

#if len(oxy_list) == 1:
#    oxy_val = int(oxy_list.value.to_numpy()[0], 2)
       
#print(f'oxy_list: {oxy_list} oxy: {oxy_val}')

# %%
