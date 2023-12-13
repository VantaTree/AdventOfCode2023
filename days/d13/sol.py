print("Day 13:")

def check_horizontal(grid, i):
    left, right = i-1, i+2
    while True:
        if left<0 or right>=len(grid):
            return True
        if grid[left] != grid[right]:
            return False
        left -= 1
        right += 1

def check_vertical(grid, i):
    left, right = i-1, i+2
    while True:
        if left<0 or right>=len(grid[0]):
            return True
        l_grid = [ln[left] for ln in grid]
        r_grid = [ln[right] for ln in grid]
        if l_grid != r_grid:
            return False
        left -= 1
        right += 1

FILE = "days/d13/main.txt"

grid_list = [[]]
sum1 = 0

with open(FILE) as f:
    for line in f.read().splitlines():
        if line == "":
            grid_list.append([])
            continue
        grid_list[-1].append(line)

for c, grid in enumerate(grid_list):
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:
            if check_horizontal(grid, i):
                sum1 += (i+1)*100
                break

    if i < len(grid)-2: continue
    for j in range(len(grid[0])-1):
        l_grid = [ln[j] for ln in grid]
        r_grid = [ln[j+1] for ln in grid]
        if l_grid == r_grid:
            if check_vertical(grid, j):
                sum1 += j+1
                break


print("Part 1:", sum1)
print("Part 2:")
