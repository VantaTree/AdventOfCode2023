def manhattan_dist(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)


def step_counter(steps, start):
    active = {start}

    for _ in range(steps):

        new_active = set()

        for node in active:

            px, py = node
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                x, y = px+dx, py+dy
                if x < 0 or y < 0 or x >= size or y >= size:
                    continue
                if grid[y][x] == "#":
                    continue
                new_active.add((x, y))

        active = new_active
    return len(active)


print("Day 21:")

FILE = "days/d21/example.txt"
FILE = "days/d21/main.txt"

STEPS = 26501365

grid = []

with open(FILE) as f:
    for y, line in enumerate(f.read().splitlines()):
        grid.append(list(line))
        for x, ch in enumerate(line):
            if ch != "S": continue
            grid[y][x] = "."
            start = x, y
            break
# print(*grid, sep="\n")
size = len(grid)
half_size = size//2


directions = ((1, 0), (1, 1), (0, 1), (0, 0))
dd_start = ((0.5, 1), (0, 0.5), (0.5, 0), (1, 0.5))
radius = STEPS // size
mid_parts = radius/2 * (radius-1)*4 + 1
sum2 = 0
sum2 += ((mid_parts)//2-radius+1)*step_counter((size)*2-1, (0, 0))
sum2 += ((mid_parts)//2+radius)*step_counter((size-1)*2, (0, 0))

for i in range(4):
    x, y = directions[i]
    x0, y0 = directions[i-1]

    sum2 += step_counter(size-1, ( int((size-1)*dd_start[i][0]), int((size-1)*dd_start[i][1]) ))
    sum2 += radius*step_counter(size//2-1, ((size-1)*x, (size-1)*y))
    sum2 += (radius-1)*step_counter(size-1+size//2, ((size-1)*x, (size-1)*y))

print("Part 1:")
print("Part 2:", sum2)
