
import re
from functools import cache

#@cache
def variations(token, numbers, depth=0):
    results = 0
    for i in range(depth, len(token)):
        if token[i] == '?':
            results += variations(token.replace("?", ".", 1), numbers, i+1)
            results += variations(token.replace("?", "#", 1), numbers, i+1)
    
    results += is_valid(token, numbers)
    return results





token = "?###???????? 3,2,1"

def is_valid(seq, numbers):
    if '?' in seq:
        return False
    results = re.finditer(r"\#+", seq)
    items = []
    for r in results:
        items.append(list(r.span()))

    if len(items) != len(numbers):
        return False
    else:
        for i in range(len(items)-1):
            if items[i-1][1] == items[i][0]:
                return False
        for item, num in zip(items, numbers):
            if item[1]-item[0] != int(num):
                return False
    return True


# token = "???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"
# seq, numbers = token.split(" ")
# numbers = numbers.split(",")
# print(variations(seq, tuple(numbers)))

with open("data.txt") as f:
    lines = f.read().split("\n")
    s = 0
    for i, l in enumerate(lines):
        print(i, l)
        seq, numbers = l.split(" ")
        numbers = numbers.split(",")
        r = variations(seq, tuple(numbers))
        print("-->", r)
        s += r

    print(s)
        #print(variations(seq, numbers))