print("Day 21:")

FILE = "days/d21/example.txt"
FILE = "days/d21/main.txt"

with open(FILE) as f:
    grid = f.read().splitlines()
    for y, line in enumerate(grid):
        try: x = line.index("S")
        except ValueError: continue
        grid[y] = line[:x] + "." + line[x+1:]
        start = x, y
        break

# print(*grid, sep="\n")

w, h = len(grid[0]), len(grid)
active = {start}

for _ in range(64):

    new_active = set()

    for node in active:

        px, py = node
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            x, y = px+dx, py+dy
            if x < 0 or y < 0 or x >= w or y >= h:
                continue
            if grid[y][x] == "#":
                continue
            new_active.add((x, y))

    active = new_active


print("Part 1:", len(active))
print("Part 2:")
