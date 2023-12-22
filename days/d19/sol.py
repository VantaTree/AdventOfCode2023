print("Day 19:")

FILE = "days/d19/example.txt"
FILE = "days/d19/main.txt"

parts = []
workflows = {}
in_parts = False
# xmas

with open(FILE) as f:
    for line in f.read().splitlines():
        if not line:
            in_parts = True
            continue

        if in_parts:
            line = line[1:-1]
            x, m, a, s = [int(num.split("=")[1]) for num in line.split(",")]
            parts.append((x, m, a, s))
        else:
            name, other = line.split("{")
            instructions = []
            for ins in other[:-1].split(","):
                if ":" not in ins:
                    instructions.append(ins)
                else:
                    other, target = ins.split(":")
                    piece = "xmas".index(other[0])
                    sign = other[1]
                    num = int(other[2:])
                    instructions.append((piece, sign, num, target))
            workflows[name] = instructions

sum1 = 0
for part in parts:
    x, m, a, s = part
    work = "in"
    while True:
        if work == "A":
            sum1 += x+m+a+s
            break
        elif work == "R":
            break
        for ins in workflows[work]:
            if isinstance(ins, str):
                work = ins
                break
            piece, sign, num, target = ins
            if (part[piece] > num) if sign == ">" else (part[piece] < num):
                work = target
                break
    print(work)

print("Part 1:", sum1)
print("Part 2:")
