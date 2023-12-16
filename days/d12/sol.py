print("Day 12:")

def calc_contagious_grps(rec, assume_question_as_working=True):
    seq = [0]
    in_grp = False
    for ch in rec:
        if ch == "." or (ch == "?" if assume_question_as_working else 0):
            if in_grp:
                seq.append(0)
            in_grp = False
        else:
            seq[-1] += 1
            in_grp = True
    return (seq[:-1] if seq[-1] == 0 else seq)


def calc_permutations(rec:list[str], seq:list[int], index:int):

    cal_seq = calc_contagious_grps(rec)
    # print(cal_seq)
    # print("".join(rec))
    if sum(cal_seq) > sum(seq):
        return 0
    if cal_seq == seq and rec.count("?") == 0:
        return 1
    if index == len(rec):
        return 0

    perms = 0
    for ch in rec[index:]:
        index += 1
        if ch != "?":
            continue
        rec_hash = rec[:index-1] + ["#"] + rec[index:]
        rec_dot = rec[:index-1] + ["."] + rec[index:]
        perms += calc_permutations(rec_hash, seq, index)
        perms += calc_permutations(rec_dot, seq, index)
        break
    
    return perms


FILE = "days/d12/main.txt"

records:list[tuple[str, list[int]]] = []
sum1 = 0

with open(FILE) as f:
    for line in f.read().splitlines():
        
        rec, seq = line.split(" ")
        seq = [int(n) for n in seq.split(",")]
        records.append((rec, seq))

# print(*records, sep="\n")

for rec, seq in records:

    one = calc_permutations(list(rec), seq, 0)
    sum1 += one

print("Part 1:", sum1)
print("Part 2:")
