
import itertools
from copy import deepcopy
from collections import deque


def to_matrix(lines):
    items = []
    for l in lines:
        print(l)
        items.append([i for i in l])
    return items

moves = {
    "U" : [0, -1],
    "D" : [0, 1],
    "L" : [-1, 0],
    "R" : [1, 0]
}

graph = {}

def find_max(next, end, visited, steps, depth=0):

    if depth < 10: # for debugging only..
        print(next, end, steps, depth)
    if next == end:
        return steps
    
    nums = []
    for node in graph[next]:
        point, s = node
        if point in visited:
            continue
        nums.append(find_max(point, end, visited + tuple([point]), steps+s, depth+1))
    
    if nums:
        return max(nums)
    else:
        return 0



    

def find_bps(matrix, start):
    visited = set()
    queue = [start]

    results = []
    
    while queue:
        next = queue.pop()
        visited.add(next)
        x, y = next
        nexts = []
        for d in [(0,1, 'v'), (0, -1, "^"), (1, 0, ">"), (-1, 0, "<")]:
            new_p = (x + d[0], y + d[1])
            if new_p[0] < 0 or new_p[0] >= len(matrix[0]) or new_p[1] < 0 or new_p[1] >= len(matrix):
                continue
            flr = matrix[new_p[1]][new_p[0]]
            if flr == '#': # hit boundry
                continue
            
            if new_p not in visited:
                nexts.append(new_p)
        
        if nexts:
            if len(nexts) >= 2:
                results.append((x, y))
            for n in nexts:
                queue.append(n)

    return results

def build_graph(matrix, bps):

    
    for current_branch in bps:
        graph[current_branch] = []
        visited = set()

        queue = deque()
        queue.append((current_branch, 1))
        while queue:
            
            pos, steps = queue.popleft()
            x, y = pos
            visited.add((x, y))
            for d in [(0,1, 'v'), (0, -1, "^"), (1, 0, ">"), (-1, 0, "<")]: 
                new_p = (x + d[0], y + d[1])
                if new_p[0] < 0 or new_p[0] >= len(matrix[0]) or new_p[1] < 0 or new_p[1] >= len(matrix):
                    continue
                if '#' == matrix[new_p[1]][new_p[0]]: # hit boundry
                    continue
                if new_p in visited:
                    continue
                if new_p in bps: # we have left a branch point
                    graph[current_branch].append((new_p, steps))
                else:
                    queue.append((new_p, steps+1))
    
    for key, value in graph.items():

        print(key, " --> ", value)

    return graph


with open("data.txt") as f:

    lines = f.read()
    lines = lines.replace(">", ".").replace("<", ".").replace("v", ".").replace("^", ".")#.replace("#", " ")
    lines = lines.split("\n")
    
    matrix = to_matrix(lines)
    for y, row in enumerate(matrix):
        print(''.join([x for x in row]))
    # start = []
    
    bps = find_bps(matrix, (1, 0))
    for b in bps:
        print(b)

    target=(lines[-1].find("."), len(matrix)-1)
    start=(1, 0)
    g = build_graph(matrix, [start] + bps + [target])
    s = find_max(start, target, tuple([start]), 0)
    print(s)
    

    exit()
    for y, row in enumerate(matrix):
        for x, col in enumerate(matrix):
            if (x, y) in bps:
                matrix[y][x] = "X"
            if matrix[y][x] == '#':
                matrix[y][x] = " "

    for y, row in enumerate(matrix):    
        print(''.join([x for x in row]))
    # results = bfs(matrix, (1, 0, 0, 'v'), target=(lines[-1].find("."), len(matrix)-1))
    # print(results)
    #print(max([i[3] for i in results]))



