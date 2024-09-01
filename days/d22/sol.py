from collections import defaultdict

print("Day 22:")

FILE = "days/d22/example.txt"
FILE = "days/d22/main.txt"

class Box:

    def __init__(self, x, y, z, w, d, l):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
        self.d = d
        self.l = l

    def collidebox(self, other) -> bool:
        
        return self.x + self.w > other.x and \
                self.x < other.x + other.w and \
                self.y + self.d > other.y and \
                self.y < other.y + other.d and \
                self.z + self.l > other.z and \
                self.z < other.z + other.l
    
    def move(self, x=0, y=0, z=0):
        return Box(self.x+x, self.y+y, self.z+z, self.w, self.d, self.l)
    
    def copy(self):
        return Box(self.x, self.y, self.z, self.w, self.d, self.l)
    
    def __str__(self):
        return F"<Box: x:{self.x} y:{self.y} z:{self.z} w:{self.w} d:{self.d} l:{self.l}>"
    
    def __hash__(self):
        return hash((self.x, self.y, self.z, self.w, self.d, self.l))
    

bricks:list[Box] = []
bricks_up :defaultdict[set[Box]] = defaultdict(set)
bricks_down:defaultdict[set[Box]] = defaultdict(set)

with open(FILE) as f:
    for line in f.read().splitlines():
        pos1, pos2 = line.split("~")
        x1, y1, z1 = map(int, pos1.split(","))
        x2, y2, z2 = map(int, pos2.split(","))
        bricks.append(Box(x1, y1, z1, x2-x1+1, y2-y1+1, z2-z1+1))

# droping the bricks
bricks.sort(key = lambda b: b.z)
for brick in bricks:
    cz = brick.z
    while True:
        if brick.z == 1: break
        colliding = False
        for check_brick in bricks:
            if brick == check_brick: continue
            sb = check_brick.move(z=1)
            if brick.collidebox(sb):
                colliding = True
                bricks_up[check_brick].add(brick)
                bricks_down[brick].add(check_brick)
        if colliding: break
        brick.z -= 1 # apply the change


# Part 1
# can be destroyed safely -> chain reaction
count = 0
for brick in bricks:
    all_supported = True
    for dependent in bricks_up[brick]:
        depends_on = False
        for support in bricks_down[dependent]:
            if support != brick:
                depends_on = True
                break
        if not depends_on:
            all_supported = False
            break
    if all_supported:
        count += 1


# part 2
# count all possible destructions -> chain reaction
bricks.sort(key = lambda b: b.z, reverse=True)

def get_demo_count(brick, bricks_demolished):
    
    if brick in bricks_demolished:
        return bricks_demolished
    
    bricks_demolished.add(brick)
    unstable_blocks = []

    for dependent in bricks_up[brick]:
        is_supported = False
        for support in bricks_down[dependent]:
            if support not in bricks_demolished:
                is_supported = True
                break
        if not is_supported:
            unstable_blocks.append(dependent)

    for dependent in unstable_blocks:
        get_demo_count(dependent, bricks_demolished)

count2 = 0
for brick in bricks:
    bd = set()
    get_demo_count(brick, bd)
    count2 += len(bd)-1
                
# for brick in bricks:
#     print(brick)
# print()

# print("Bricks: supporting")
# for brick, brick_set in bricks_up.items():
#     print(brick, "---=")
#     for b in brick_set:
#         print("\t", b)
# print()

# print("Bricks: supported by")
# for brick, brick_set in bricks_up.items():
#     print(brick, "---=")
#     for b in brick_set:
#         print("\t", b)
# print()

print("Part 1:", count)
print("Part 2:", count2)
