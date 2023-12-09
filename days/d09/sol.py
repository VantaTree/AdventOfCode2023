print("Day 09:")
FILE = "days/d09/main.txt"

sum1 = 0
sum2 = 0
numbers:list[list[list[int]]] = []

with open(FILE) as f:
    for line in f.read().splitlines():
        numbers.append([[int(n) for n in line.split(" ")]])

for block in numbers:
    while True:
        part = block[-1]
        new = []
        for i in range(len(part)-1):
            new.append(part[i+1]-part[i])
        block.append(new)
        if not any(new):
            break
    for j in range(len(block)-2, -1, -1):
        block[j].append(block[j][-1] + block[j+1][-1])
    sum1 += block[0][-1]
    for j in range(len(block)-2, -1, -1):
        block[j].insert(0, block[j][0] - block[j+1][0])
    sum2 += block[0][0]


print("Part 1:", sum1)
print("Part 2:", sum2)
