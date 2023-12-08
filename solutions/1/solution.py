import regex as re

items = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
exp = '|'.join(items)

with open("data.txt") as f:
    lines = f.read().split("\n")
    
    sum = 0
    for l in lines:
        
        # part1 1
        #iters = re.findall("\d", l, overlapped=True)
        # part 2
        iters = re.findall("\d|"+exp, l, overlapped=True)
        print(iters)
        try:
            first = int(iters[0])
        except ValueError as e:
            first = items.index(iters[0])+1

        try:
            last = int(iters[-1])
        except ValueError as e:
            last = items.index(iters[-1])+1
        
        print(first, last)
        val = first*10 + last
        print(val)
        sum += val
    print(sum)
    