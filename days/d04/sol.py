print("Day 04:")
FILE = "days/d04/main.txt"
sum1 = 0
sum2 = 0
dup_case = {}

with open(FILE) as f:
    for i, line in enumerate(f.read().splitlines()):

        case, data = line.split(": ")
        winning, nums = data.split(" | ")
        winning = {int(n) for n in winning.split(" ") if n != ""}
        nums = {int(n) for n in nums.split(" ") if n != ""}

        wins = len(winning.intersection(nums))
        sum1 += 2**wins//2
        
        tickets = 1 + sum(map(lambda k:dup_case[k][1], dup_case))
        sum2 += tickets
        for k in tuple(dup_case):
            dup_case[k][0] -= 1
            if dup_case[k][0] == 0:
                del dup_case[k]
        if wins:
            dup_case[i] = [wins, tickets]
        # print(i, ":", tickets, wins)
        # print(dup_case)

print("Part 1:", sum1)
print("Part 2:", sum2)
