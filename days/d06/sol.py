print("Day 06:")
FILE = "days/d06/main.txt"

record_mul = 1 # part 1

with open(FILE) as f:
    time, dist = f.read().splitlines()

    # part 2
    time2 = int(time[11:].replace(" ", ""))
    dist2 = int(dist[11:].replace(" ", ""))

    # part 1
    time1 = [int(x) for x in time[11:].split(" ") if x != ""]
    dist1 = [int(x) for x in dist[11:].split(" ") if x != ""]

# part 1
for i in range(len(time1)):
    records1 = 0
    for t in range(time1[i]):
        if t*(time1[i]-t) > dist1[i]:
            records1 += 1
    record_mul *= records1

# part 2
for t in range(1, time2+1):
    if t*(time2-t) > dist2:
        min_hold = t-1
        break

records2 = time2-min_hold*2-1

# print(time2)
# print(dist2)
# print(min_hold)

print("Part 1:", record_mul)
print("Part 2:", records2)
