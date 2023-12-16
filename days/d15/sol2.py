print("Day 15:")

def hash_256(word):
    value = 0
    for ch in word:
        value += ord(ch)
        value *= 17
        value %= 256
    return value

# FILE = "days/d15/example.txt"
FILE = "days/d15/main.txt"

instructions = []

with open(FILE) as f:
    for word in f.read().split(","):
        if word[-1] == "-":
            label, lens = word[:-1], "-1"
        else:
            label, lens = word.split("=")
        lens = int(lens)

        instructions.append((label, lens))

boxes = [[] for _ in range(256)]

sum2 = 0
for label, lens in instructions:
    box = hash_256(label)
    if lens == -1:
        boxes[box] = [(lab, len) for (lab, len) in boxes[box] if lab != label]
        continue
    for i, bb in enumerate(boxes[box]):
        if bb[0] == label:
            boxes[box][i] = (label, lens)
            break
    else:
        boxes[box].append((label, lens))

for bn, box in enumerate(boxes, start=1):
    for i, (label, lens) in enumerate(box, start=1):
        c = i * bn * lens
        # print(c, bn, i, lens, label)
        sum2 += c


print("Part 1:")
print("Part 2:", sum2)
