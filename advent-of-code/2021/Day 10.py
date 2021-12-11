# %%
with open('Day 10 Input.txt', "r", encoding="utf-8") as fp:
    line = fp.readline().strip()

    values = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    while line:
        stack = []
        for c in line:
            if c == '(' or c == '[' or c == '<' or c == '{':
                stack.append(c) 
            else:
                test_c = stack.pop()
                if (c == ')' and test_c != '(') or \
                   (c == '>' and test_c != '<') or \
                   (c == '}' and test_c != '{') or \
                   (c == ']' and test_c != '['):
                    score += values[c]
        line = fp.readline().strip()

print(score)

# %% Part 2

with open('Day 10 Input.txt', "r", encoding="utf-8") as fp:
    line = fp.readline().strip()

    values = {'(': 1, '[': 2, '{': 3, '<': 4}
    incomplete_stacks = []
    
    while line:
        invalid_line = False
        stack = []
        for c in line:
            if c == '(' or c == '[' or c == '<' or c == '{':
                stack.append(c) 
            else:
                test_c = stack.pop()
                if (c == ')' and test_c != '(') or \
                   (c == '>' and test_c != '<') or \
                   (c == '}' and test_c != '{') or \
                   (c == ']' and test_c != '['):
                    invalid_line = True

        if not invalid_line:
            incomplete_stacks.append(stack)

        line = fp.readline().strip()

scores = []
for arr in incomplete_stacks:
    score = 0
    for c in arr[ : : -1]:
        score = 5 * score + values[c]
    scores.append(score)

import numpy as np
median = np.median(scores)