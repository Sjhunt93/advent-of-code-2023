
# from shapely.geometry import Point
# from shapely.geometry.polygon import Polygon

def bfs_floodfill(matrix, starts: list):


    visited = set()
    queue = []
    for s in starts:
        queue.append(s)
        
    while queue:
        next = queue.pop()
        matrix[next[1]][next[0]] = '~'
        visited.add(next)
        for d in [(0,1), (0, -1), (1, 0), (-1, 0)]:
            new_p = (next[0] + d[0], next[1] + d[1])
            if new_p[0] < 0 or new_p[0] >= len(matrix[0]) or new_p[1] < 0 or new_p[1] >= len(matrix):
                continue
            if matrix[new_p[1]][new_p[0]] == '#': # hit boundry
                continue
            if new_p not in visited:
                queue.append(new_p)


with open("data.txt") as f:
    dig_instructions = f.read().split("\n")

    
    path = [(0,0)]
    start = (0,0)
    current_dir = 'D'

    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    for ins in dig_instructions:
        dir, inc, col = ins.split(" ")
        #print(dir, inc, col)
        
        for i in range(0, int(inc)):
            if dir == 'R':
                path.append((path[-1][0] + 1, path[-1][1]))
            if dir == 'L':
                path.append((path[-1][0] - 1, path[-1][1]))
            if dir == 'D':
                path.append((path[-1][0], path[-1][1] + 1))
            if dir == 'U':
                path.append((path[-1][0], path[-1][1] - 1))

            max_x = max(max_x, path[-1][0])
            max_y = max(max_y, path[-1][1])
            min_x = min(min_x, path[-1][0])
            min_y = min(min_y, path[-1][1])
    # for p in path:
    #     print(p)
    
#    print(max_x, max_y)

    dig_map = []
    for i in range(abs(min_y) + max_y+3):
        dig_map.append(['.' for x in range(abs(min_x) + max_x+3)])

    for p in path:
        y = abs(min_y)+p[1]+1
        x = abs(min_x)+p[0]+1
        assert x >=0
        assert y >= 0
        dig_map[y][x] = '#'

    
    bfs_floodfill(dig_map, [(0,0), (0, len(dig_map)-1), (len(dig_map[0])-1, len(dig_map)-1), (len(dig_map[0])-1, 0)])

    # # fill
    # for row in dig_map:
    #     to_fill = []
    #     gate = False
    #     last = ''
    #     for i, c in enumerate(row):
    #         if c == '.':
    #             if gate:
    #                 to_fill.append(i)
    #             # if row[:i].count('#') == 1: # has cross one line
    #             #     to_fill.append(i)
    #         else:
    #             if last == '.' and gate:
    #                 gate = False
    #             else:
    #                 gate = True
                
    #         last = c
    #     while to_fill:
    #         row[to_fill.pop()] = '#'

    counts = 0
    for row in dig_map:
        
        print(''.join([c for c in row]))
        counts += row.count("#") + row.count(".")
    
    print(counts)

