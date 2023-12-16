#from termcolor import colored
import itertools
from copy import deepcopy

def to_matrix(lines):
    items = []
    for l in lines:
        print(l)
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

with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    print(matrix)
    m2 = deepcopy(matrix)
    visitedSet = set()
    plot_path = []
    queue = []

    queue.append([0,0, 'D'])
    visitedSet.add(tuple([0,0, 'D']))

    while queue:
        
        x, y, dir = queue.pop()
        print(x, y, dir)
        
        visitedSet.add(tuple([x, y, dir]))
        
        xm, ym = moves[dir]
        x += xm
        y += ym
        if x < 0 or x >= len(matrix[0]) or y < 0 or y >= len(matrix):
            print("\t", "out of bonds")
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
        
        #m2[y][x] = debug[dir]
        m2[y][x] = "#"
        

        for n in next_steps:
            if tuple(n) not in visitedSet:
                queue.append(n)


    #print(len(visitedSet))

        
        # for r in m2:
        #     print(''.join([i for i in r]))
        # print("\n")
    c = 1
    for r in m2:
        c += r.count("#")
    print(c)
    # for row in range(0, len(matrix)):
    #     for x in range(0, len(matrix[0])):
    #         move_rock(matrix, x, row)
    #     #print(matrix[row])
    
    # for row in range(0, len(matrix)):
    #     print(matrix[row])
    
    # r = len(matrix)
    # score = 0
    # for row in matrix:
    #     score += (row.count('O') * r)
    #     r -= 1
    
    # print(score)
    
