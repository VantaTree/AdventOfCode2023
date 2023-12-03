print("Day 03:")
FILE = "days/d03/main.txt"
# FILE = "days/d03/example.txt"

def get_number(x, y):

    start = end = x
    seen_nums.add((x, y))

    while True:
        try:
            if not schema[y][start-1].isdigit() or start-1 < 0: break
        except IndexError: break
        start -= 1
        seen_nums.add((start, y))
    while True:
        try:
            if not schema[y][end+1].isdigit() or end+1 < 0: break
        except IndexError: break
        end += 1
        seen_nums.add((end, y))
    s = schema[y][start:end+1]
    return int(s)


part_sum = 0
seen_nums = set()

with open(FILE) as f:
    schema:list[str] = list(f.readlines())

for j, line in enumerate(schema):
    for i, ch in enumerate(line):
        if ch == "." or ch.isdigit(): continue
        #look around
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                x = dx+i
                y = dy+j
                try:
                    if schema[y][x].isdigit() and (x, y) not in seen_nums and x >= 0 and y >= 0:
                        n = get_number(x, y)
                        print(n)
                        part_sum += n
                except IndexError: continue

print("Part 1:", part_sum)
print("Part 2:")
