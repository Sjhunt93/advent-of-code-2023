from copy import deepcopy
#CARD_TYPES = "AKQT98765432K"
CARD_TYPES = "AKQT98765432J" # part 2
CARD_INDEX = [k for k in CARD_TYPES]


import functools

def get_score(counts):
    score = 0
    for i, c in enumerate(counts):
        if c > 1:
            score = i * c

    return score

def compare(hand1, hand2):
    l1 = match(hand1)
    l2 = match(hand2)
    t1 = get_type(l1)
    t2 = get_type(l2)
    
    if t1 == t2:
        for x, y in zip(hand1, hand2):
            if CARD_TYPES.index(str(x)) < CARD_TYPES.index(str(y)):
                return 1
            if CARD_TYPES.index(x) > CARD_TYPES.index(y):
                return -1

    elif t1 < t2:
        return 1
    else:
        return -1

def get_type(counts):
    # for part 2 just add this
    if counts[-1]:
        jokes = counts[-1]
        min_rank = 7
        for i in range(0, len(CARD_TYPES)-1):
            a = deepcopy(counts)
            a[-1] = 0
            a[i] += jokes
            min_rank = min(min_rank, get_type(a))
        return min_rank
    else:
        s = sorted(counts)
        s.reverse()
        # print(s)
        if s[0] == 5:
            return 1
        if s[0] == 4:
            return 2
        if s[0] == 3 and s[1] == 2: # full house
            return 3
        if s[0:3] == [3,1,1]: # three of a kind
            return 4
        if s[0:3] == [2,2, 1]: # two pairs
            return 5
        if s[0:3] == [2,1, 1]: # one pair
            return 6
        return 7
    
    
def match(hand):
    counts = []
    for c in CARD_TYPES:
        counts.append(hand.count(c))
    return counts


mapping = {}
with open("data.txt") as f:
    lines = f.read().split("\n")
    for l in lines:
        hand, bet = l.split(" ")
        mapping[hand] = int(bet)

sorted_l = sorted(mapping.keys(), key=functools.cmp_to_key(compare)) # Sort with key
print(sorted_l)

score = 0
for i, s in enumerate(sorted_l):
    score  += mapping[s] * (i + 1)

print(score)

#print(get_type(match("KTJJT")))

# #print(compare("KK677", "KTJJT"))
# print(compare("QQQJA", "T55J5"))

# hands = ["32T3K", "T55J5", "KK677", "KTJJT", "QQQJA"]

# #sorted_l = sorted(hands, key=lambda x, y: compare(x, y)) # Sort with key

# sorted_l = sorted(hands, key=functools.cmp_to_key(compare)) # Sort with key
# print(sorted_l)


# # 32T3K 765
# # T55J5 684
# # KK677 28
# # KTJJT 220
# # QQQJA 483