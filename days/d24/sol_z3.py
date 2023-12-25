import z3

print("Day 24:")

FILE = "days/d24/example.txt"
FILE = "days/d24/main.txt"

hail_stones = []

with open(FILE) as f:
    for line in f.read().splitlines():

        pos, vel = line.split(" @ ")
        px, py, pz = list(map(int, pos.split(", ")))
        dx, dy, dz = list(map(int, vel.split(", ")))
        hail_stones.append((px, py, pz, dx, dy, dz))

x = z3.Int("x")
y = z3.Int("y")
z = z3.Int("z")

dx = z3.Int("dx")
dy = z3.Int("dy")
dz = z3.Int("dz")

sol = z3.Solver()
for i, (px, py, pz, dx2, dy2, dz2) in enumerate(hail_stones[:3]):
    t = z3.Int(F"t{i}")
    sol.add(t >= 0 )
    sol.add(px + dx2 * t == x + dx * t)
    sol.add(py + dy2 * t == y + dy * t)
    sol.add(pz + dz2 * t == z + dz * t)


assert sol.check() == z3.sat

print("Part 1:")
print("Part 2:", sol.model().eval(x + y + z))
