
import re
from math import lcm


def custom_lcm(values: list):
    increments = [v for v in values]
    while len(set(values)) != 1:
        i = values.index(min(values))
        values[i] += increments[i]
        print(values[i])
    return values[0]

test = [18, 126, 9, 7, 56, 12]
print(custom_lcm(test), lcm(*test))




mapping = {}
with open("data.txt") as f:
    instructions, cords = f.read().split("\n\n")
    print(instructions)
    for ins in cords.split("\n"):
        input, left, right = re.findall("\w\w\w", ins)
        #print(input, left, right)
        mapping[input] = {
            "L" : left,
            "R" : right
    }

    # part 1
    # count =0    
    # current = "AAA"
    # index = 0
    # while current != "ZZZ":
    #     dir = instructions[index]
    #     current = mapping[current][dir]
    #     index = (index + 1) % len(instructions)
    #     count += 1

    # print(count)
    
    # part 2
    starts = []
    for key, value in mapping.items():
        if key[2] == "A":
            starts.append(key)
        
    print(starts)
    
    counts = [0 for i in range(0, len(starts))]
    index = 0
    10818234074807
    364244854835
    def is_finished(starts):
        for s in starts:
            if s[2] != "Z":
                return False
        return True

    while not is_finished(starts):
        dir = instructions[index]
        for i in range(len(starts)):
            if starts[i][2] != "Z":
                starts[i] = mapping[starts[i]][dir]
                counts[i] += 1
        index = (index + 1) % len(instructions)
        if index == 0:
            print(starts)
        
    
    print(counts)
    print(lcm(*counts))
    #print(custom_lcm(counts))
    

        