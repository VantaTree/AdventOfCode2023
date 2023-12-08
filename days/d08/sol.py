from itertools import cycle
from queue import Queue
from math import lcm

print("Day 08:")
FILE = "days/d08/main.txt"

node_map = {}
start_nodes = []
min_nums = []
aaa_node_index = None

with open(FILE) as f:
    for i, line in enumerate(f.read().splitlines()):
        if i == 0:
            steps = line
            continue
        elif i == 1: continue
        node, lr = line.split(" = ")
        node_map[node] = lr[1:4], lr[6:9]
        if node[-1] == "A":
            start_nodes.append(node)
            min_nums.append(1)
            if node == "AAA":
                aaa_node_index = len(start_nodes)-1

for i, node in enumerate(start_nodes):
    c_steps = cycle(steps)
    for count, next_step in enumerate(c_steps):
        node = node_map[node][0 if next_step == "L" else 1]
        if node[-1] == "Z":
            break
    min_nums[i] = count+1


# print(node_map)
# print(min_nums)

print("Part 1:", min_nums[aaa_node_index])
print("Part 2:",  lcm(*min_nums))
