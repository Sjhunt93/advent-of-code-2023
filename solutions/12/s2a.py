
import re
from functools import cache, lru_cache

calls = 0
#dfs_cache = {}
@lru_cache
def variations(token, numbers, depth=0):
    if token.count('#.') > len(numbers):
        return 0
    # key = token + '_'.join(numbers)
    # if key in dfs_cache:
    #     return dfs_cache[key]
    
    results = 0
    # if '#.' in token.split("?")[0]:
    #     if not is_valid(token, numbers[0:group]):
    #         return 0
    
    state = is_valid_2(token, numbers)
    #print(token, state)
    if state == 'invalid':
        return 0
    
    global calls
    calls += 1
    #while '?' in token:
    for i in range(depth, len(token)):
        if token[i] == '?':
            
            a = token.replace("?", ".", 1)
            b = token.replace("?", "#", 1)
            return variations(a, numbers, i+1) + variations(b, numbers, i+1)
    
    # dfs_cache[key] = is_valid_2(token, numbers) == 'valid'
    # return dfs_cache[key]
    return int(is_valid_2(token, numbers) == 'valid')
    #return results


def is_valid_2(seq, numbers):
    breaks = []
    num_inc = 0
    c = -1
    gap = True
    seq += "."
    for i in range(len(seq)):
        
        if seq[i] == '?':
            return 'partial'
        elif seq[i] == '#':
            if c == -1:
                c = i
        elif c != -1:
            if num_inc == len(numbers) or i-c != int(numbers[num_inc]) or not gap:
                return 'invalid'
            c = -1
            num_inc += 1
            gap = False

        if seq[i] == '.':
            gap = True
    if num_inc != len(numbers):
        return 'invalid'

        
    return 'valid'

print(is_valid_2(".###..##.", [3,2]))
print(is_valid_2(".###?.##.", [3,2]))
print(is_valid_2(".###..######", [3,2, 1]))

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

###?????????###?????????###?????????###?????????###???????? ['3', '2', '1', '3', '2', '1', '3', '2', '1', '3', '2', '1', '3', '2', '1']

token = "???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"
seq, numbers = token.split(" ")
numbers = numbers.split(",")
#print(variations(seq, numbers))
# print(variations(seq, tuple(numbers)))


with open("data.txt") as f:
    lines = f.read().split("\n")
    s = 0
    for i, l in enumerate(lines):
        print(i, l)
        seq, numbers = l.split(" ")
        #seq = ''.join([seq + "?" for i in range(5)])[:-1]
        print(seq)
        numbers = numbers.split(",")
        n2 = []
        for i in range(0, 5):
            n2.extend(numbers)
        
        print(seq, n2)
        #r = variations(seq, tuple(n2))
        r = variations(seq, tuple(numbers))
        print("-->", r)
        s += r

    print(s, calls)
        #print(variations(seq, numbers))