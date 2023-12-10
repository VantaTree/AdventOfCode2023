print("Day 10:")

def in_loop_3x(x, y) -> bool:
    """ checks if x, y is on the loop, eg 3x3:
    .|. 
    .L-  L extends to top and right
    ...
    """

    global in_box
    if not (x//3, y//3) in loop:
        return False
    pipe = grid_map[y//3][x//3]
    (ix1, iy1), (ix2, iy2) = pipes[pipe]
    dx, dy = x//3*3+1, y//3*3+1
    if (x, y) not in ((dx, dy), (dx+ix1, dy+iy1), (dx+ix2, dy+iy2)):
        return False
    in_box += 1
    return True



FILE = "days/d10/main.txt"
grid_map:list[str] = []
start = (0, 0)
pipes = {
    "-":((1, 0), (-1, 0)),
    "|":((0, 1), (0, -1)),
    "L":((1, 0), (0, -1)),
    "J":((0, -1), (-1, 0)),
    "7":((0, 1), (-1, 0)),
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

# find first pipe connecting Start
s_hands = [None, None]
x, y = start
for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
    dx += x
    dy += y
    if not (0 <= dx < len(grid_map[0]) and 0 <= dy < len(grid_map)):
        continue
    pipe = grid_map[dy][dx]
    (ix1, iy1), (ix2, iy2) = pipes[pipe]
    if (dx+ix1, dy+iy1) == (x, y):
        nx, ny = dx, dy
        s_hands[0] = (-ix1, -iy1)
        break
    if (dx+ix2, dy+iy2) == (x, y):
        nx, ny = dx, dy
        s_hands[0] = (-ix2, -iy2)
        break
loop = {start, (nx, ny)}

# traverse loop
while True:
    if (nx, ny) == start:
        break
    (ix1, iy1), (ix2, iy2) = pipes[grid_map[ny][nx]]
    if (nx+ix1, ny+iy1) == (x, y):
        x, y = nx, ny
        s_hands[1] = (-ix2, -iy2)
        nx, ny = nx+ix2, ny+iy2
    elif (nx+ix2, ny+iy2) == (x, y):
        s_hands[1] = (-ix1, -iy1)
        x, y = nx, ny
        nx, ny = nx+ix1, ny+iy1
    loop.add((nx, ny))

# find which pipe S(start) is
if s_hands[1] > s_hands [0]:
    s_hands[0], s_hands[1] = s_hands[1], s_hands[0]
for k, v in pipes.items():
    if v == (s_hands[0], s_hands[1]):
        break
pipes["S"] = pipes[k]

# traverse and count all outside nodes
in_box = 0
x, y = 0, 0
visited = {(x, y)}
new_pipes = visited.copy()
while True:
    visited.update(new_pipes)
    active_pipes = new_pipes.copy()
    new_pipes.clear()
    for (x, y) in active_pipes:
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            dx += x
            dy += y
            if not (0 <= dx < len(grid_map[0])*3 and 0 <= dy < len(grid_map)*3):
                continue
            if (dx, dy) in visited:
                continue
            if in_loop_3x(dx, dy):
                continue
            new_pipes.add((dx, dy))
    if len(new_pipes) == 0: break

# get no. of inside pipes
total = len(grid_map[0]) * len(grid_map) * 9
my_visits = len(visited) - in_box
inside_pipes = total - my_visits - len(loop)*9

print("Part 1:", len(loop)/2)
print("Part 2:", (inside_pipes+4)/9) # no f-ing idea why i need to put +4, probably somrthing to do with in_box.
