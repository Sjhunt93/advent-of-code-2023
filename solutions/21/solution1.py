
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

def bfs(matrix, start, limit):


    visited = set()
    queue = [start]
    plots = set()
    while queue:
        next = queue.pop()
        
        visited.add(next)
        plots.add((start[0], start[1]))

        time = next[2] + 1
        for d in [(0,1), (0, -1), (1, 0), (-1, 0)]:
            new_p = (next[0] + d[0], next[1] + d[1])
            if new_p[0] < 0 or new_p[0] >= len(matrix[0]) or new_p[1] < 0 or new_p[1] >= len(matrix):
                continue
            if matrix[new_p[1]][new_p[0]] == '#': # hit boundry
                continue
            
            if time >= limit:
                continue
            step = (new_p[0], new_p[1], time)
            if step not in visited:
                queue.append(step)
            # if (new_p[0], new_p[1]) not in visited:
            #     queue.append(step)
            plots.add((new_p[0], new_p[1]))
        print(len(queue))
    print(len(plots)+1)
    count = 0
    for v in visited:
        if v[2] == limit - 1:
            count += 1
    print(count)

    # for p in plots:
    #     matrix[p[1]][p[0]] = 'O'

with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    start = []
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if matrix[y][x] == 'S':
                start = (x, y, 0)

    bfs(matrix, start, 65)
   

    # for y, row in enumerate(matrix):
    #     print(''.join([x for x in row]))

