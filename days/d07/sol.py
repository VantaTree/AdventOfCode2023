from collections import Counter

print("Day 07:")

def insertion_sort(arr, arr2):

    for i in range(1, len(arr)):
        key = arr[i]
        key2 = arr2[i]
        j = i-1
        while j>=0 and cmp_card(key, arr[j]): 
            arr[j+1] = arr[j]
            arr2[j+1] = arr2[j]
            j -= 1
        arr[j+1] = key
        arr2[j+1] = key2

def cmp_card(card1, card2) -> bool:
    
    c1, c2 = Counter(card1), Counter(card2)
    
    j1 = c1.get("J", 0)
    j2 = c2.get("J", 0)
    
    if j1 != 0 and j1 < 5:
        del c1["J"]
        c1[max(c1, key=lambda k:c1[k])] += j1
    if j2 != 0 and j2 < 5:
        del c2["J"]
        c2[max(c2, key=lambda k:c2[k])] += j2
        
    c1 = sum([v*v for v in c1.values()])
    c2 = sum([v*v for v in c2.values()])
    
    if c1 != c2:
        return c1 < c2
    else:
        for c1, c2 in zip(card1, card2):
            c1 = card_value[c1]
            c2 = card_value[c2]
            if c1 != c2:
                return c1 < c2
        return False


FILE = "days/d07/main.txt"

cards:list[str] = []
bids:list[int] = []
card_value = {c:i for c, i in zip("AKQT98765432J", range(12, -1, -1))}

with open(FILE) as f:
    for line in f.read().splitlines():
        card, bid = line.split(" ")
        cards.append(card)
        bids.append(int(bid))

sum1 = 0

insertion_sort(cards, bids)
for i, (card, bid) in enumerate(zip(cards, bids), start=1):
    sum1 += i*bid

print("Part 1:")
print("Part 2:", sum1)
