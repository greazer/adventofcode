# %%
from calendar import day_abbr
from ctypes import create_unicode_buffer
from xml.sax.handler import DTDHandler



with open("Day 8 Input Test.txt") as fp:
    line = fp.readline()
    count_1_4_7_8 = 0
    while line:
        output_values = line.strip().split("|")[1].strip().split(" ")
        output_values

        for o in output_values:
            if len(o) == 2 or len(o) == 3 or len(o) == 4 or len(o) == 7:
                count_1_4_7_8 += 1
        line = fp.readline()

count_1_4_7_8

# %%

# %%
with open("Day 8 Input Test.txt") as fp:
    line = fp.readline()

    mapping= {}

    for i in range(0,9):
        mapping[i] = None

    lines = []
    while line:
        lines.append(line)
        line = fp.readline()
#%%

for line in lines:
    input_output = line.strip().split('|');
    input_values = input_output[0].strip().split(' ')

    for str in input_values:
        if len(str) == 2:
            mapping[1] = str
        elif len(str) == 3:
            mapping[7] = str
        elif len(str) == 4:
            mapping[4] = str
        elif len(str) == 7:
            mapping[8] = str
# %%
for line in lines:
    input_output = line.strip().split('|');
    input_values = input_output[0].strip().split(' ')
    for str in input_values:
        if len(str) == 6:
            mapping[6] = str if all([char in mapping[1] for char in str]) else ''
            if len(mapping[6]) > 0:
                break


# %%
# acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab |
# cdfeb fcadb cdfeb cdbaf

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

digit_defs = {'0': '012456', '1': '25', '2': '02346', '3': '02356', '4': '1235', '5':'01356', '6':'013456', '7':'024', '8':'0123456', '9':'012356'}

# 1 = ab
# 4 = eafb
# 7 = dab
# 8 = acedgfb 
# 2 has to be the 5 letters with no 'b' = gcdfa
# 5 has to be the 5 letters with no 'a' = cdfbe
# 6 has to be the 6 letters with no 'a' = cdfbeg
# Therefore pos 4 must be the extra letter between 5 and 6 = 'g'
# 9 has to be the 6 letters with no 'g': cefabd
# 0 has to be the other 6 letters with a 'g': cagedb
# Therefore pos 3 must be the extra letter between 0 and 8 = 'f'
# 3 is the remaining 5 letter = fbcad

# 0, 6, 9 
# 9 is either cefabd or cdfgeb or cagedb



# %%
