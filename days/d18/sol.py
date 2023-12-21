print("Day 18:")

FILE = "days/d18/example.txt"
FILE = "days/d18/main.txt"

data= []
direction = {"R": (1,0), "L": (-1,0), "U": (0,-1), "D": (0,1)}
with open(FILE) as f:
    for line in f.read().splitlines():
        dir, st, col = line.split()
        col = col[1:-1]
        data.append([dir, int(st)])

# follow dig instructions
x, y = 0, 0
min_p = [x, y]
max_p = [x, y]
loop = {(x, y)}
for dir, st in data:
    dx, dy = direction[dir]
    for _ in range(st):
        x, y = x+dx, y + dy
        loop.add((x, y))
        if min_p[0] > x:
            min_p[0] = x
        if min_p[1] > y:
            min_p[1] = y
        if max_p[0] < x:
            max_p[0] = x
        if max_p[1] < y:
            max_p[1] = y


# find one inside tile
in_y = min_p[1]+1
got_in = False
for in_x in range(min_p[0], max_p[0]+1):
    if (in_x, in_y) in loop:
        got_in = True
    elif got_in:
        break

# determine inside tiles (flood fill)
visited = set()
active = {(in_x, in_y)}
while active:
    x, y = active.pop()
    if x < min_p[0] or x > max_p[0] or y < min_p[1] or y > max_p[1]:
        continue
    if (x, y) in visited or (x, y) in loop:
        continue
    visited.add((x, y))
    for dx, dy in ((1, 0), (0, 1), (-1, 0), (0, -1)):
        active.add((x+dx, y+dy))


w, h = (max_p[0]-min_p[0]+1), (max_p[1]-min_p[1]+1)
total = w*h
inside = len(visited) + len(loop)

# visualization
# f = open("days/d18/ok.txt", "a")
# grid = ["."*w for _ in range(h)]
# for y in range(h):
#     for x in range(w):
#         if (x+min_p[0], y+min_p[1]) in loop:
#             # print("#", end="")
#             f.write("#")
#         else:
#             f.write(".")
#             # print(".", end="")
#     # print()
#     f.write("\n")
# f.close()

print("Part 1:", inside)
print("Part 2:")
