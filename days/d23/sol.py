import sys
sys.setrecursionlimit(10000)

print("Day 23:")

FILE = "days/d23/example.txt"
FILE = "days/d23/main.txt"

grid:list[str] = []
with open(FILE) as f:
    grid = f.read().splitlines()

dirs = {">": (1, 0), "<": (-1, 0), "v": (0, 1), "^": (0, -1)}
start_pos = 1, 0
end_pos = len(grid[0])-2, len(grid)-1

def longest_path(x, y, visited:set[tuple[int, int]]):

    if (x, y) == end_pos:
        return 0
    
    if grid[y][x] in dirs:
        dx, dy = dirs[grid[y][x]]
        nx, ny = x+dx, y+dy
        if (nx, ny) in visited:
            return 1
        visited.add((nx, ny))
        return longest_path(nx, ny, visited)+1
    
    max_step = float("-inf")
    for dx, dy in dirs.values():

        nx, ny = x+dx, y+dy

        if nx < 0 or nx >= len(grid[0]) or ny < 0 or ny >= len(grid):
            continue
        if grid[ny][nx] == "#":
            continue
        if (nx, ny) in visited:
            continue

        new_visited = visited.copy()
        new_visited.add((nx, ny))
        step_count = longest_path(nx, ny, new_visited)+1
        max_step = max(step_count, max_step)

    return max_step

steps = longest_path(*start_pos, {start_pos})

print("Part 1:", steps)
