print("Day 14:")

FILE = "days/d14/main.txt"

with open(FILE) as f:
    grid = f.read().splitlines()

sum1 = 0

for x in range(len(grid[0])):
    base = 0
    for y in range(len(grid)):
        rock = grid[y][x]
        if rock == "#":
            base = y+1
        elif rock == "O":
            base += 1
            sum1 += len(grid)-base+1

print("Part 1:", sum1)
print("Part 2:")
