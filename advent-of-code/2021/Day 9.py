# %%
import numpy as np
import pandas as pd

# %%
class CaveMap:
    def __init__(self, filename):
        with open(filename, "r", encoding="utf-8") as ifile:
            self._map = np.loadtxt(ifile, dtype=str)
            self._mapwidth = len(self._map[0])
            self._maplen = len(self._map)

    def isLocationLow(self, row, col):
        test_val = self._map[row][col]
        if row == 0 and col == 0:
            return int(self._map[row][col + 1] > test_val) and int(
                self._map[row + 1][col] > test_val
            )
        elif row == 0 and col == self._mapwidth - 1:
            return int(self._map[row][col - 1] > test_val) and int(
                self._map[row + 1][col] > test_val
            )
        elif row == self._maplen - 1 and col == 0:
            return int(self._map[row - 1][col] > test_val) and int(
                self._map[row][col + 1] > test_val
            )
        elif row == self._maplen - 1 and col == self._mapwidth - 1:
            return int(self._map[row - 1][col] > test_val) and int(
                self._map[row][col - 1] > test_val
            )
        elif row == 0:
            return (
                int(self._map[row][col - 1] > test_val)
                and int(self._map[row][col + 1] > test_val)
                and int(self._map[row + 1][col] > test_val)
            )
        elif col == 0:
            return (
                int(self._map[row - 1][col] > test_val)
                and int(self._map[row][col + 1] > test_val)
                and int(self._map[row + 1][col] > test_val)
            )
        elif row == self._maplen - 1:
            return (
                int(self._map[row][col - 1] > test_val)
                and int(self._map[row][col + 1] > test_val)
                and int(self._map[row - 1][col] > test_val)
            )
        elif col == self._mapwidth - 1:
            return (
                int(self._map[row - 1][col] > test_val)
                and int(self._map[row][col - 1] > test_val)
                and int(self._map[row + 1][col] > test_val)
            )
        else:
            return (
                int(self._map[row - 1][col] > test_val)
                and int(self._map[row][col - 1] > test_val)
                and int(self._map[row][col + 1] > test_val)
                and int(self._map[row + 1][col] > test_val)
            )

# 2199943210
# 3987894921
# 9856789892
# 8767896789
# 9899965678

    def findBasinSizeFor(self, row, col):
        size = 0

        if int(self._map[row][col]) < 9:
            size = 1
            replace_str = self._map[row][:col] + "9" + self._map[row][col + 1 :]
            self._map[row] = replace_str
            if col - 1 >= 0:
                size += self.findBasinSizeFor(row, col - 1)
            if col + 1 < self._mapwidth:
                size += self.findBasinSizeFor(row, col + 1)
            if row - 1 >= 0:
                size += self.findBasinSizeFor(row - 1, col)
            if row + 1 < self._maplen:
                size += self.findBasinSizeFor(row + 1, col)

        return size
# %%
map = CaveMap("Day 9 Input Test.txt")

low_count = 0
val = 0
for r in range(0, len(map._map)):
    for c in range(0, map._mapwidth):
        if map.isLocationLow(r, c):
            print(f"{r},{c}: {map._map[r][c]}")
            low_count += 1
            val += int(map._map[r][c]) + 1

print(f"{low_count}, {val}")


# %%
map = CaveMap("Day 9 Input.txt")

lowspots = []
for r in range(0, len(map._map)):
    for c in range(0, map._mapwidth):
        if map.isLocationLow(r,c):
            lowspots.append([r,c])

basinsizes = []
for lowspot in lowspots:
    orig_map = map._map.copy()
    basinsizes.append(map.findBasinSizeFor(lowspot[0], lowspot[1]))
    map._map = orig_map.copy()

arr = np.array(basinsizes)
sorted_index_array = np.argsort(arr)
sorted_array = arr[sorted_index_array]

top3 = sorted_array[-3:]
result = top3[0] * top3[1] * top3[2]
result

# %%
