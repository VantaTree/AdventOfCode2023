print("Day 10:")
FILE = "days/d10/main.txt"

grid_map:list[str] = []
start = (0, 0)
pipes = {
    "-":((-1, 0), (1, 0)),
    "|":((0, -1), (0, 1)),
    "L":((1, 0), (0, -1)),
    "J":((-1, 0), (0, -1)),
    "7":((-1, 0), (0, 1)),
    "F":((1, 0), (0, 1)),
    ".":((0, 0), (0, 0))
    }

with open(FILE) as f:
    for y, line in enumerate(f.read().splitlines()):
        grid_map.append(line)
        if (x:=line.find("S")) >= 0:
            start = (x, y)

# print(start)
# print(*grid_map, sep="\n")

x, y = start
loop_length = 1
for ddx, ddy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    dx = x+ddx
    dy = y+ddy
    if (0 <= dx < len(grid_map[0]) and 0 <= dy < len(grid_map)):
        pipe = grid_map[dy][dx]
        (ix1, iy1), (ix2, iy2) = pipes[pipe]
        if (dx+ix1, dy+iy1) == (x, y):
            nx, ny = dx, dy
            break
        if (dx+ix2, dy+iy2) == (x, y):
            nx, ny = dx, dy
            break

while True:

    if (nx, ny) == start:
        break
    (ix1, iy1), (ix2, iy2) = pipes[grid_map[ny][nx]]
    if (nx+ix1, ny+iy1) == (x, y):
        x, y = nx, ny
        nx, ny = nx+ix2, ny+iy2
    elif (nx+ix2, ny+iy2) == (x, y):
        x, y = nx, ny
        nx, ny = nx+ix1, ny+iy1
    loop_length += 1


print("Part 1:", (loop_length)/2)
print("Part 2:")
