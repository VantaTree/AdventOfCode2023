print("Day 13:")

def check_horizontal(grid, i, diff):
    left, right = i-1, i+2
    while True:
        if left<0 or right>=len(grid):
            return diff
        diff += check_row(grid[left], grid[right])
        if diff >= 2:
            return 99
        left -= 1
        right += 1

def check_vertical(grid, i, diff):
    left, right = i-1, i+2
    while True:
        if left<0 or right>=len(grid[0]):
            return diff
        diff += check_col(grid, left, right)
        if diff >= 2:
            return 99
        left -= 1
        right += 1

def check_row(ln_a, ln_b):

    diff = 0
    for a, b in zip(ln_a, ln_b):
        if a != b:
            diff += 1
            if diff > 1:
                return 99
    return diff

def check_col(grid, i1, i2):

    diff = 0
    ln_a = [ln[i1] for ln in grid]
    ln_b = [ln[i2] for ln in grid]
    for a, b in zip(ln_a, ln_b):
        if a != b:
            diff += 1
            if diff > 1:
                return 99
    return diff


FILE = "days/d13/main.txt"

grid_list = [[]]
sum2 = 0

with open(FILE) as f:
    for line in f.read().splitlines():
        if line == "":
            grid_list.append([])
            continue
        grid_list[-1].append(line)

for c, grid in enumerate(grid_list):
    for i in range(len(grid)-1):
        diff = check_row(grid[i], grid[i+1])
        if diff < 2:
            diff = check_horizontal(grid, i, diff)
            if 0 < diff < 2:
                sum2 += (i+1)*100
                break

    if i < len(grid)-2: continue
    for j in range(len(grid[0])-1):
        diff = check_col(grid, j, j+1)
        if diff < 2:
            diff = check_vertical(grid, j, diff)
            if 0 < diff < 2:
                sum2 += j+1
                break


print("Part 1:")
print("Part 2:", sum2)
