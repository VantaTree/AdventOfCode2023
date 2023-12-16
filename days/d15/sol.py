print("Day 15:")

FILE = "days/d15/example.txt"
# FILE = "days/d15/main.txt"

with open(FILE) as f:
    sequence = f.read().split(",")

sum1 = 0
for word in sequence:
    value = 0
    for ch in word:
        value += ord(ch)
        value *= 17
        value %= 256
    print(value)
    sum1 += value


print("Part 1:", sum1)
print("Part 2:")
