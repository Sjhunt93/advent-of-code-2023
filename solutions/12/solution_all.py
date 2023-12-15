
import re
from functools import cache

calls = 0
#dfs_cache = {}

token = "???.###????.###????.###????.###????.### 1,1,3,1,1,3,1,1,3,1,1,3,1,1,3"
seq, numbers = token.split(" ")
numbers = [int(n) for n in numbers.split(",")]


def split_into_tokens(seq):
    xx = [s + "#." for s in seq.split("#.")]
    xx[-1] = xx[-1][:-2]

    return [x for x in xx if x]

@cache
def validate(token_left, numbers_left):
    print(token_left, numbers_left)

    tokens = split_into_tokens(token_left)
    for i, t in enumerate(tokens):
        if '?' in t:
            break
        if  t.count('#') != numbers_left[0]:
            return 0
        else:
            numbers_left = numbers_left[1:]
            token_left = token_left[len(t):]
            if '#' in token_left and not numbers_left:
                return 0
            if not numbers_left:
                break

    if numbers_left and not token_left:
        return 0
    if not numbers_left and '#' not in token_left:
        return 1

    for i in range(0, len(token_left)):
        if token_left[i] == '?':
            
            a = token_left.replace("?", ".", 1)
            b = token_left.replace("?", "#", 1)
            return validate(a, tuple(list(numbers_left))) + validate(b, tuple(list(numbers_left)))
    
    return 1

def variations(token, numbers, depth=0):
    for i in range(depth, len(token)):
        if token[i] == '?':
            
            a = token.replace("?", ".", 1)
            b = token.replace("?", "#", 1)
            return variations(a, numbers, i+1) + variations(b, numbers, i+1)


token = "?###???????? 3,2,1"
seq, numbers = token.split(" ")
numbers = [int(n) for n in numbers.split(",")]
# seq = "##?..#?..#..#..#"
# nums = [2,2,1,1,1]
print(validate(seq, tuple(numbers)))


with open("data.txt") as f:
    lines = f.read().split("\n")
    s = 0
    for i, l in enumerate(lines):
        print(i, l)
        seq, numbers = l.split(" ")
        seq = ''.join([seq + "?" for i in range(5)])[:-1]
        numbers = [int(n) for n in numbers.split(",")]
        n2 = []
        for i in range(0, 5):
            n2.extend(numbers)
        
        print(seq, numbers)
        #r = variations(seq, tuple(n2))
        r = validate(seq, tuple(n2))
        print("-->", r)
        s += r

    print(s, calls)
        #print(variations(seq, numbers))