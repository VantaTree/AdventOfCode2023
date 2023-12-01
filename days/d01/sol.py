print("Day 01:")
FILE = "days/d01/main.txt"

nums = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]

def num_match(string, rev=False):
    for i, num_str in enumerate(nums):
        if (not rev and string.startswith(num_str)) or (rev and string.endswith(num_str)):
            return i
    return None

sum = 0

with open(FILE) as f:
    for line in f.readlines():
        for i, ch in enumerate(line):
            if ch.isdigit():
                sum += int(ch) * 10
                break
            elif (n := num_match(line[i:])) is not None:
                sum += n * 10
                break
        for i, ch in enumerate(line[::-1]):
            if ch.isdigit():
                sum += int(ch)
                break
            elif (n := num_match(line[0:len(line) - i], True)) is not None:
                sum += n
                break


print("Part 1:")
print("Part 2:", sum)
