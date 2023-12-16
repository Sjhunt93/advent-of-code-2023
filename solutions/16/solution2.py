#from termcolor import colored
import itertools
from copy import deepcopy

def to_matrix(lines):
    items = []
    for l in lines:
        #print(l)
        items.append([i for i in l])
    return items

# HELPER
#print(hscore, vscore)
# for y, row in enumerate(matrix):
#     print(row)
#     for x, col in enumerate(row):
#         c = matrix[y][x]



moves = {
    "U" : [0, -1],
    "D" : [0, 1],
    "L" : [-1, 0],
    "R" : [1, 0]
}

# /
ref1 = {
    "R" : "U",
    "D" : "L",
    "U" : "R",
    "L" : "D"
}
#\\
ref2 = {
    "R" : "D",
    "D" : "R",
    "L" : "U",
    "U" : "L"
}
debug = {
    "R" : ">",
    "L" : "<",
    "U" : "^",
    "D" : "v"
}

def get_score(matrix, start):
    queue = []
    visitedSet = set()
    results = set()

    queue.append(start)
    visitedSet.add(tuple(start))

    
    while queue:
        
        x, y, dir = queue.pop()
        #print(x, y, dir)
        
        visitedSet.add(tuple([x, y, dir]))
        
        xm, ym = moves[dir]
        x += xm
        y += ym
        if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix):
            #print("\t", "out of bonds")
            continue
        
        c = matrix[y][x]
        next_steps = []
        
        if c == '|' and dir in "LR":
            next_steps.append([x,y, "U"])    
            next_steps.append([x,y, "D"])
        elif c == "-" and dir in "UD":
            next_steps.append([x,y, "L"])    
            next_steps.append([x,y, "R"])
        elif c == "/":
            next_steps.append([x,y, ref1[dir]])
        elif c == "\\":
            next_steps.append([x,y, ref2[dir]])
        else:
            
            next_steps.append([x,y, dir])
        
        results.add(tuple([x, y]))

        for n in next_steps:
            if tuple(n) not in visitedSet:
                queue.append(n)

    return len(results) + 1



with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    max_val = 0
    for i in range(0, len(matrix[0])):
        a = get_score(matrix, [i, 0, "D"])
        b = get_score(matrix, [i, len(matrix)-1, "U"])
        max_val = max(max_val, a, b)
    
    for i in range(0, len(matrix)):
        a = get_score(matrix, [0, i, "R"])
        b = get_score(matrix, [len(matrix[0])-1, i, "L"])
        max_val = max(max_val, a, b)  
    print(max_val)
    