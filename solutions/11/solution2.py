#from termcolor import colored
import itertools



LARGER = 1000000-1

def to_matrix(lines):
    items = []
    for l in lines:
        items.append([i for i in l])
    return items

def move_down(after_y, galaxies):
    for galaxy, position in galaxies.items():
        if position[1] > after_y:
            position[1] += LARGER

def move_right(after_x, galaxies):
    for galaxy, position in galaxies.items():
        if position[0] > after_x:
            position[0] += LARGER

def distance(a, b, galaxies):
    dis = abs(galaxies[a][0]-galaxies[b][0]) + abs(galaxies[a][1]-galaxies[b][1])
    print(dis)
    return dis

with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    print(matrix)
    stack = []
    score = 0
    position = []
    
    galaxies = {}
    i = 1
    for y, row in enumerate(matrix):
        print(row)
        for x, col in enumerate(row):
            c = matrix[y][x]
            if c == '#':
                galaxies[i] = [x, y]
                i += 1
    
    

    
    # # expand rows
    # new_lines = []
    new_lines = 0
    for y, row in enumerate(matrix):
        if '#' not in row:
            move_down(y+new_lines, galaxies)
            new_lines += LARGER
    print(galaxies)
    #         new_lines.append(list(row))
    #     new_lines.append(list(row))

    new_cols = 0
    for x in range(0, len(matrix[0])):
        expand = True
        for y in range(0, len(matrix)):
            if matrix[y][x] == '#':
                expand = False
        if expand:
            print("expanding")
            move_right(x+new_cols, galaxies)
            new_cols += LARGER
    print(galaxies)

    for y, row in enumerate(matrix):
        for x, col in enumerate(row):
            print(col, end="")
        print("")



    pairs = {}
    for r in itertools.product(galaxies.keys(), galaxies.keys()): 
        
        k_1 = f"{r[0]}_{r[1]}"
        k_2 = f"{r[1]}_{r[0]}"
        if k_1 not in pairs and k_2 not in pairs and r[0] != r[1]:
            pairs[k_1] = distance(r[0], r[1], galaxies)
            
    #print(pairs)
    print(galaxies)
    s = 0
    for key, val in pairs.items():
        s += val
    print(s)


