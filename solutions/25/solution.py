import itertools
from collections import deque
from random import seed
from random import randint
import time

seed(int(time.time()))

connections = {}
nodes = set()
singles = set()
edges = {}
# In this example, if you disconnect the wire between hfx/pzl, the wire between bvb/cmg, and the wire between nvd/jqt, you will divide the components into two separate, disconnected groups:
START = "vlk"

def trace_2(connections, start, end, ignore):
    queue = deque()
    visited = set()
    queue.append((start, [start]))
    
    while queue:
        current, path = queue.popleft()
        if current == end:
            return path
            
        visited.add(current)
        
        for i in connections[current]:
            if (i, current) in ignore or (current, i) in ignore: # dont try this
                continue
            if i not in visited:
                queue.append((i, path+[i]))

    return path

def trace_all(connections, start, end, ignore):
    queue = deque()
    visited = set()
    queue.append(start)
    
    while queue:
        x = queue.popleft()
        if x == end:
            break
        visited.add(x)
        
        for i in connections[x]:
            if (i, x) in ignore or (x, i) in ignore: # dont try this
                continue
            if i not in visited:
                queue.append(i)
    return visited



with open("data.txt") as f:
    lines = f.read().split("\n")
    for l in lines:
        a, b = l.split(":")
        items = b.strip().split(" ")
        if a in connections:
            connections[a] += items
        else:
            connections[a] = items
            
        nodes.add(a)
        for i in items:
            nodes.add(i)
            if i in connections:
                connections[i] += [a]
            else:
                connections[i] = [a]

            l = [a, i]
            l.sort()
            singles.add((l[0], l[1]))



    for s in singles:
        edges[s] = 0

    nodes = list(nodes)

    for cycle in range(0, 1000):
        a = randint(0, len(nodes)-1)
        b = randint(0, len(nodes)-1)
        path = trace_2(connections, nodes[a], nodes[b], [])
        for i in range(1, len(path)):
                l = [path[i-1], path[i]]
                l.sort()
                edges[(l[0], l[1])] += 1


    print(edges)
    edges_sorted = {k: v for k, v in sorted(edges.items(), key=lambda item: item[1])}
    print(edges_sorted)

    to_filter = []
    for key, value in edges_sorted.items():
        to_filter.append(key)

    # take the top most items
    to_filter = to_filter[-8:]
    print("\n\n", to_filter, len(to_filter))

    options = itertools.combinations(to_filter, 3)
    default = len(trace_all(connections, START, "...", []))
    print(default, len(to_filter))

    i = 0
    for o in options:
        i += 1
        print(list(o))
        v = trace_all(connections, START, "...", list(o))
        print(v)
        if len(v) != default:
            print(len(v), o)
            print("group 1", len(v), "group 2", default-len(v))
            print(len(v) * (default-len(v)))
            assert False
        print(i)

                