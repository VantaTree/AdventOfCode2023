print("Day 16:")

def trace_beam(pos, direc):
     
    visited = set()
    active = [(*pos, *direc)]
    energized = set()

    while len(active) > 0:

        x, y, dx, dy = active.pop()
        # x, y = x+dx, y+dy
        if x < 0 or x >= len(grid[0]) or y < 0 or y >= len(grid):
            continue
        if (x, y, dx, dy) in visited:
            continue
        visited.add(((x, y, dx, dy)))
        mirr = grid[y][x]
        # if mirr != ".":
        energized.add((x, y))
        if mirr == "." or (mirr == "|" and x == 0) or (mirr == "-" and y == 0):
            active.append((x+dx, y+dy, dx, dy))
        if mirr == "|":
            active.append((x, y+1, 0, 1))
            active.append((x, y-1, 0, -1))
        if mirr == "-":
            active.append((x+1, y, 1, 0))
            active.append((x-1, y, -1, 0))
        if mirr == "/":
            active.append((x-dy, y-dx, -dy, -dx))
        if mirr == "\\":
            active.append((x+dy, y+dx, dy, dx))

    return len(energized)


# FILE = "days/d16/example.txt"
FILE = "days/d16/main.txt"

pos = (0, 0)
direction = (1, 0)

with open(FILE) as f:
    grid = f.read().splitlines()

sum1 = trace_beam((0, 0), (1, 0))
sum2 = 0
for x in range(len(grid[0])):
    a = trace_beam((x, 0), (0, 1))
    b = trace_beam((x, len(grid)-1), (0, -1))
    sum2 = max(sum2, a, b)

for y in range(len(grid[0])):
    a = trace_beam((0, y), (1, 0))
    b = trace_beam((len(grid[0])-1, y), (-1, 0))
    sum2 = max(sum2, a, b)

print("Part 1:", sum1)
print("Part 2:", sum2)
