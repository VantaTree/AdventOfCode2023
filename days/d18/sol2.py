from math import gcd

print("Day 18:")

FILE = "days/d18/example.txt"
FILE = "days/d18/main.txt"

data= []
direction = {"R": (1,0), "L": (-1,0), "U": (0,-1), "D": (0,1)}
perimeter = 0
with open(FILE) as f:
    for line in f.read().splitlines():
        dir, st, col = line.split()
        col = col[1:-1]
        # part 2
        st = int(col[1:-1], 16)
        dir = "RDLU"[int(col[-1])]
        perimeter += st
        data.append([dir, st])

# get verticies
x, y = 0, 0
verticies = [(0, 0)]
for dir, st in data:
    dir = direction[dir]
    x, y = x+dir[0]*st, y+dir[1]*st
    verticies.append((x, y))

# calc area
area = 1
for i in range(-1, len(verticies)-1):
    x1, y1 = verticies[i]
    x2, y2 = verticies[i+1]
    area += (x1*y2 - x2*y2)
# area //= 2

print("Part 1:", area + perimeter//2)
print("Part 2:")
