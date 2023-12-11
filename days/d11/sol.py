print("Day 11:")

def euclid_dist(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

FILE = "days/d11/main.txt"

with open(FILE) as f:
    grid_map = f.read().splitlines()

galaxies = []
sum1 = 0
sum2 = 0
g_rows = [1] * len(grid_map) # y
g_cols = [1] * len(grid_map[0]) # x
expansion = 1000000-1

# add galaxies
for j, line in enumerate(grid_map):
    for i, ch in enumerate(line):
        if ch == "#":
            galaxies.append((i, j))
            g_rows[j] = 0
            g_cols[i] = 0

# g_rows stores the number of rows empty to the ;eft of a specific y index
empty_r = 0
empty_c = 0
for i, (gr, gc) in enumerate(zip(g_rows, g_cols)):
    empty_r += gr
    empty_c += gc
    g_rows[i] = empty_r
    g_cols[i] = empty_c

# calc distance
for i, (x1, y1) in enumerate(galaxies):
    for (x2, y2) in galaxies[i+1:]:
        sum1 += euclid_dist(x1+g_cols[x1], y1+g_rows[y1],
                            x2+g_cols[x2], y2+g_rows[y2])
        sum2 += euclid_dist(x1+g_cols[x1]*expansion, y1+g_rows[y1]*expansion,
                            x2+g_cols[x2]*expansion, y2+g_rows[y2]*expansion)

print("Part 1:", sum1)
print("Part 2:", sum2)
