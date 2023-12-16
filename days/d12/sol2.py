from functools import cache

print("Day 12:")

@cache
def calc_permutations(rec:str, seq:tuple):

    if not rec:
        return not seq
    if not seq:
        return "#" not in rec

    if rec[0] == "?":
        return calc_permutations("#"+rec[1:], seq) + calc_permutations("."+rec[1:], seq)
    if rec[0] == ".":
        return calc_permutations(rec[1:], seq)
    if len(rec) >= seq[0] and all(ch != "." for ch in rec[:seq[0]]) and (len(rec) == seq[0] or rec[seq[0]] != "#"):
        return calc_permutations(rec[seq[0]+1:], seq[1:])
    
    return 0


FILE = "days/d12/main.txt"

records:list[tuple[str, list[int]]] = []
sum2 = 0

with open(FILE) as f:
    for line in f.read().splitlines():
        
        rec, seq = line.split(" ")
        seq = [int(n) for n in seq.split(",")]
        records.append((rec, tuple(seq)))

# print(*records, sep="\n")

for rec, seq in records:

    rec = "?".join([rec]*5)
    seq = seq*5
    one = calc_permutations(rec, seq)
    sum2 += one
    # print(one)

print("Part 1:")
print("Part 2:", sum2)
