print("Day 14:")

# FILE = "days/d14/example.txt"
FILE = "days/d14/main.txt"

rocks = set()
new_rocks = set()

with open(FILE) as f:
    grid = f.read().splitlines()
    for y, line in enumerate(grid):
        for x, ch in enumerate(line):
            if ch == "O":
                rocks.add((x, y))

cycles_sum = []

for cycle in range(200):
    # north
    for x in range(len(grid[0])):
        base = 0
        for y in range(len(grid)):
            if grid[y][x] == "#":
                base = y+1
            elif (x, y) in rocks:
            # elif rock == "O":
                base += 1
                new_rocks.add((x, base-1))            
                # sum1 += len(grid)-base+1
    rocks.clear()
    rocks.update(new_rocks)
    new_rocks.clear()

    # west
    for y in range(len(grid)):
        base = 0
        for x in range(len(grid[0])):
            if grid[y][x] == "#":
                base = x+1
            elif (x, y) in rocks:
            # elif rock == "O":
                base += 1
                new_rocks.add((base-1, y))            
                # sum1 += len(grid)-y
    rocks.clear()
    rocks.update(new_rocks)
    new_rocks.clear()

    # south
    for x in range(len(grid[0])):
        base = len(grid)-1
        for y in range(len(grid)):
            y = len(grid)-y-1
            if grid[y][x] == "#":
                base = y-1
            elif (x, y) in rocks:
            # elif rock == "O":
                new_rocks.add((x, base)) 
                base -= 1
                # sum1 += len(grid)-base-1
    rocks.clear()
    rocks.update(new_rocks)
    new_rocks.clear()

    sum2 = 0
    # east
    for y in range(len(grid)):
        base = len(grid[0])-1
        for x in range(len(grid[0])):
            x = len(grid[0])-x-1
            if grid[y][x] == "#":
                base = x-1
            elif (x, y) in rocks:
            # elif rock == "O":
                base -= 1
                new_rocks.add((base+1, y))            
                sum2 += len(grid)-y
    rocks.clear()
    rocks.update(new_rocks)
    new_rocks.clear()
    cycles_sum.append(sum2)
    # print(cycle, ":", sum2)

# draw grid
# for y in range(len(grid)):
#     for x in range(len(grid[0])):
#         if grid[y][x] == "#":
#             print("#", end="")
#         elif (x, y) in rocks:
#             print("O", end="")
#         else: print(".", end="")
#     print()

# find the 1_000_000_000th cycle answer yourself lol
n = 1000000000
offset = 91
loop = 63
nth = (n-offset) % 63
answer = cycles_sum[offset+nth-1]
# print(*cycles_sum)
print("Part 1:")
print("Part 2:", answer)
