from itertools import combinations

print("Day 24:")

FILE = "days/d24/example.txt"
FILE = "days/d24/main.txt"

# min_pos = 7
# max_pos = 27
min_pos = 200000000000000
max_pos = 400000000000000

hail_stones = []

with open(FILE) as f:
    for line in f.read().splitlines():

        pos, vel = line.split(" @ ")
        px, py, pz = list(map(int, pos.split(", ")))
        dx, dy, dz = list(map(int, vel.split(", ")))
        hail_stones.append((px, py, pz, dx, dy, dz))

def is_intersecting(x1, y1, x2, y2, x3, y3, x4, y4):
    
    a = (x4 - x3)*(y3 - y1) - (y4 - y3)*(x3 - x1)
    c = (x2 - x1)*(y3 - y1) - (y2 - y1)*(x3 - x1)
    b = (x4 - x3)*(y2 - y1) - (y4 - y3)*(x2 - x1)
    if b == 0:
        return False
    if a == 0 and c == 0:
        return True
    alpha = a/b
    beta  = c/b
    if not(0 <= alpha <= 1 and 0 <= beta <= 1):
        return False
    xx = x1 + alpha*(x2 - x1)
    yy = y1 + alpha*(y2 - y1)
    if min_pos <= xx <= max_pos and min_pos <= yy <= max_pos:
        return True
    return False


intersection = 0
for (px1, py1, _, dx1, dy1, _), (px2, py2, _, dx2, dy2, _) in combinations(hail_stones, 2):

    intersection += is_intersecting(px1, py1,
                                    px1+dx1*max_pos, py1+dy1*max_pos,
                                    px2, py2,
                                    px2+dx2*max_pos, py2+dy2*max_pos)


print("Part 1:", intersection)
print("Part 2:")
