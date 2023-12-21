from queue import PriorityQueue

print("Day 17:")

FILE = "days/d17/example.txt"
FILE = "days/d17/main.txt"

grid:list[list[int]] = []
start = (0, 0)

with open(FILE) as f:
    for line in f.read().splitlines():
        grid.append([int(n) for n in line])
        
end = len(grid[0])-1, len(grid)-1

def find_min_heat(min_st, max_st):
        
    visited = {}
    next = PriorityQueue()
    next.put((0, 0, 0, 1, 0, 1))
    next.put((0, 0, 0, 0, 1, 1))

    while not next.empty():
        node = next.get()
        heat, x, y, dx, dy, st = node
        x, y = x+dx, y+dy
        if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
            continue
        heat += grid[y][x]
        if (x, y) == end and st >= min_st:
            return heat
        if (x, y, dx, dy, st) in visited: continue
        visited[(x, y, dx, dy, st)] = heat
        if st >= min_st:
            # right
            next.put((heat, x, y, -dy, dx, 1))
            # left
            next.put((heat, x, y, dy, -dx, 1))
        # straight
        if st < max_st:
            next.put((heat, x, y, dx, dy, st+1))

# print(*grid, sep="\n")
print("Part 1:", find_min_heat(1, 3))
print("Part 2:", find_min_heat(4, 10))
