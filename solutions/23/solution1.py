
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


# moves = {
#     "^" : [0, -1],
#     "v" : [0, 1],
#     "<" : [-1, 0],
#     ">" : [1, 0]
# }
# opposite = {"<": ">", ">": "<", "v": "^", "^": "v"}


moves = {
    "U" : [0, -1],
    "D" : [0, 1],
    "L" : [-1, 0],
    "R" : [1, 0]
}

def bfs(matrix, start, target):


    visited = set()
    queue = [(start, start)]

    results = []
    while queue:
        next, prev = queue.pop()
        
        

        x, y, time, dir = next
        px, py, _, _ = prev
        visited.add((x, y, dir))
        
        if (x, y) == target:
            results.append(next)

        for d in [(0,1, 'v'), (0, -1, "^"), (1, 0, ">"), (-1, 0, "<")]:
            new_p = (x + d[0], y + d[1])
            if new_p[0] < 0 or new_p[0] >= len(matrix[0]) or new_p[1] < 0 or new_p[1] >= len(matrix):
                continue
            # don't allow us going back..
            if new_p[0] == px and new_p[1] == py:
                continue

            flr = matrix[new_p[1]][new_p[0]]
            if flr == '#': # hit boundry
                continue
            # if flr != '.' and flr != d[2]:
            #     continue

            
            
            step = (new_p[0], new_p[1], time+1, d[2])
            if step not in visited:
            #if (new_p[0], new_p[1], d[2]) not in visited:
                queue.append((step, next))

        print(len(queue))
    
    return results

with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    start = []
    

    results = bfs(matrix, (1, 0, 0, 'v'), target=(lines[-1].find("."), len(matrix)-1))
    print(results)
    print(max([i[2] for i in results]))

    # for y, row in enumerate(matrix):
    #     print(''.join([x for x in row]))

