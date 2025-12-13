# import sys
# sys.setrecursionlimit(10000)
from collections import defaultdict
from queue import Queue
class Stack(list):
    def put(self, *args, **kwargs):
        return super().append(*args, **kwargs)
    def get(self, *args, **kwargs):
        return super().pop(*args, **kwargs)
    def empty(self):
        return len(self) == 0

print("Day 23:")

FILE = "days/d23/example.txt"
# FILE = "days/d23/main.txt"

grid:list[str] = []
with open(FILE) as f:
    for line in f.read().splitlines():
        grid.append(list(line))

dirs = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
grid[0][1] = "#"
node_network:dict[tuple[int, int], dict[tuple[int, int], int]] = defaultdict(dict)
start_pos = 1, 1
end_pos = len(grid[0])-2, len(grid)-1

# node_q = Queue()
node_q = Stack()
visited = {(*start_pos,)}
node_q.put((*start_pos, *start_pos, 0))

while not node_q.empty():

    x, y, tx, ty, count = node_q.get()

    ways = []
    for dx, dy in dirs.values():
        nx, ny = x+dx, y+dy

        if (x, y) == end_pos:
            continue
        if grid[ny][nx] == "#":
            continue
        if (nx, ny) in visited:
            continue
        ways.append((nx, ny))
        visited.add((nx, ny))

    if len(ways) == 1:
        nx, ny = ways[0]
        node_q.put((nx, ny, tx, ty, count+1))
    else:
        for nx, ny in ways:
            node_q.put((nx, ny, nx, ny, 0))
        node_network[(tx, ty)][(x, y)] = count
        node_network[(x, y)][(tx, ty)] = count

print(node_network[(*end_pos,)])
print(node_network[(*start_pos,)])
print(node_network[(3, 5)])
print(node_network[(13, 13)])
    


steps = 0
print("Part 2:", steps)
