
import itertools
from copy import deepcopy
from collections import deque, defaultdict
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
    steps_vs_time = defaultdict(int)
    while queue:
        next = queue.pop()
        
        visited.add(next)
        steps_vs_time[next[2]] = steps_vs_time[next[2]] + 1
        plots.add((start[0], start[1]))

        time = next[2] + 1
        
        for d in [(0,1), (0, -1), (1, 0), (-1, 0)]:
            # x = next[0] + d[0]
            # y = next[1] + d[1]
            
            # if x < 0:
            #     x += len(matrix[0])
            # elif x >= len(matrix[0]):
            #     x -= len(matrix[0])

            # if y < 0:
            #     y += len(matrix)
            # elif y >= len(matrix):
            #     y -= len(matrix)

            # new_p = (x, y)
            new_p = (next[0] + d[0], next[1] + d[1])

            # if
            # if new_p[0] < 0 or new_p[0] >= len(matrix[0]) or new_p[1] < 0 or new_p[1] >= len(matrix):
            #     continue
            if matrix[new_p[1] % len(matrix[0])][new_p[0] % len(matrix)] == '#': # hit boundry
                continue
            
            if time >= limit:
                continue
            step = (new_p[0], new_p[1], time)
            if step not in visited:
                queue.append(step)
            # if (new_p[0], new_p[1]) not in visited:
            #     queue.append(step)
            #plots.add((new_p[0], new_p[1]))
        print(len(queue))
    
    # count = 0
    # for v in visited:
    #     if v[2] == limit - 1:
    #         count += 1
    # print(count)

    # for l in range(limit-1, 0, -1):
    #     count = 0
    #     for v in visited:
    #         if v[2] == l:
    #             count += 1
    #     print(l, count)
        

    print(steps_vs_time)
    # for p in plots:
    #     matrix[p[1]][p[0]] = 'O'
    return steps_vs_time


with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    start = []
    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            if matrix[y][x] == 'S':
                start = (x, y, 0)
                break

    # 65, 65 + 131, 65 + 131*2
    results = bfs(matrix, start, 65+131*2+1)
    f0 = results[65]
    f1 = results[65+131]
    f2 = results[65+131*2]
    print(f0, f1, f2)
    
    # this bit is not mine... :(
    # quadratic form is y = ax^2 + bx + c
    # let x = 0
    # therefore c = f0
    # y - c - bx = a
    c = f0
    a = (f2 - 2*f1 + f0) // 2
    b = f1 - f0 - a

    f = lambda n: a*n**2 + b*n + c
    result = f((26501365 - 65) // 131)
    print(result)

    #bfs(matrix, start, 131)
    # a2x2 + a1x + a0
    #3778 33833 93864
    # for y, row in enumerate(matrix):
    #     print(''.join([x for x in row]))

