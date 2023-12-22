print("Day 19:")

def calc_poss(work_path):

    max_parts = [4001]*4
    min_parts = [0]*4
    for piece, sign, num in work_path:
        if sign == ">" and min_parts[piece] < num:
            min_parts[piece] = num
        elif sign == "<" and max_parts[piece] > num:
            max_parts[piece] = num

    poss = 1
    for m1, m2 in zip(min_parts, max_parts):
        poss *= m2-m1-1
        
    return poss


def work_path(work:str, path:list[tuple]):

    if work == "A":
        return calc_poss(path)
    elif work == "R":
        return 0

    poss = 0
    for ins in workflows[work]:
        if isinstance(ins, str):
            poss += work_path(ins, path.copy())
        else:
            piece, sign, num, target = ins
            path2 = path.copy()
            path2.append((piece, sign, num))
            poss += work_path(target, path2)

            n_sign = ">" if sign == "<" else "<"
            num += 1 if n_sign == "<" else -1
            path.append((piece, n_sign, num))

    return poss


FILE = "days/d19/example.txt"
FILE = "days/d19/main.txt"

workflows = {}
in_parts = False
# xmas

with open(FILE) as f:
    for line in f.read().splitlines():
        if not line:
            in_parts = True
            break
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


print("Part 1:")
print("Part 2:", work_path("in", []))
