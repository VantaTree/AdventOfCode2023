from collections import defaultdict
from itertools import combinations
from queue import Queue

print("Day 25:")

FILE = "days/d25/example.txt"
FILE = "days/d25/main.txt"

components = defaultdict(list)
connections = set()

with open(FILE)as f:
    for line in f.read().splitlines():
        name, comps = line.split(": ")
        comps = comps.split(" ")
        components[name] = comps
        for c in comps:
            connections.add(tuple(sorted([name, c])))

for name, comps in tuple(components.items()):
    for com in comps:
        components[com].append(name)
# print(components)
# print(connections)
# print(len(connections))
        
total_components = len(components)

for comb in combinations(connections, 3):
    conn = connections - set(comb)
    visited = set()
    visited_cuts = set()
    next = Queue()
    visited.add(comb[0][0])
    visited_cuts.add(comb[0][0])
    next.put(comb[0][0])
    new_components = 0
    while not next.empty():

        curr_node = next.get()
        new_components += 1
        if new_components >= total_components: break
        for connected in components[curr_node]:

            the_connection = (curr_node, connected) if connected > curr_node else (connected, curr_node)
            if the_connection not in conn: continue
            if connected in visited: continue
            if connected == comb[0][1]:
                new_components = total_components
                break
            for a, b in comb:
                if (connected == a and b in visited_cuts) or (connected == b and a in visited_cuts):
                    new_components = total_components
                    break
                if connected in (a, b):
                    visited_cuts.add(connected)
            visited.add(connected)
            next.put(connected)

    if new_components < total_components:
        # print(new_components * (total_components-new_components))
        break

    

print("Part 1:", new_components * (total_components-new_components))
print("Part 2:")
