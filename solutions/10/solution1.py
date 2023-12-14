from termcolor import colored


directions = {
    "U" : [0, -1],
    "D" : [0, 1],
    "L" : [-1, 0],
    "R" : [1, 0]
}

def to_matrix(lines):
    items = []
    for l in lines:
        items.append([i for i in l])
    return items

def get_adjacents(xi, yi, matrix):
    
    results = {}
    for key, value in directions.items():
        try:
            y = yi+value[1]
            x = xi+value[0]
            if x == -1 or y == -1:
                raise Exception("")
            #results[key] = {'val' : matrix[y][x], "pos" : [x, y]} 
            results[key] = [matrix[y][x], x, y]
        except:
            results[key] = None
    return results
    
    counts = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            try:
                #print(matrix[y+yi][x+xi], y+yi,x+xi )
                counts += int(matrix[y+yi][x+xi] not in ['.'] + nums)
            except Exception as e:
                pass
    print("\t-->", counts)
    return counts

def can_connect(current, target, direction):
    if current == "S":
        return True
    if target == "S":
        return False

    # if direction == "R" and current not in ["|"]:
    #     return target in ["J", "-", "7"]
    #valid_going_right = []
    if current in ["-", "L", "F"] and direction == "R":
        return target in ["J", "-", "7"]
    if current in ["-", "J", "7"] and direction == "L":
        return target in ["F", "L", "-"]
    if current in ["|", "L", "J"] and direction == "U":
        return target in ["|", "F", "7"]
    if current in ["|", "F", "7"] and direction == "D":
        return target in ["|", "L", "J"]
    
    return False
        
    

assert can_connect("-", "J", "R")
assert can_connect("-", "7", "R")
#assert can_connect("-", "7", "R")


with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    print(matrix)
    stack = []
    score = 0
    position = []
    
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            c = matrix[y][x]
            if c == "S":
                position = [x, y]
                break
    

    visited = set()
    print(position)
    adjacents = get_adjacents(position[0], position[1], matrix)
    # head1 = adjacents["R"]
    # head2 = adjacents["D"]
    head1 = adjacents["L"]
    head2 = adjacents["U"]
    print(head1, head2)

    visited.add(tuple(["S", position[0], position[1]]))
    visited.add(tuple(head1))
    visited.add(tuple(head2))
    
    i = len(visited)
    #while i == len(visited):
    while head1 != head2 and i == len(visited):
        adjacents1 = get_adjacents(head1[1], head1[2], matrix)
        adjacents2 = get_adjacents(head2[1], head2[2], matrix)
        
        for dir, item in adjacents1.items():
            if item and can_connect(head1[0], item[0], dir) and tuple(item) not in visited:
                head1 = adjacents1[dir]
                break
        
        
        for dir, item in adjacents2.items():
            if item and can_connect(head2[0], item[0], dir) and tuple(item) not in visited:
                head2 = adjacents2[dir]
                
                break
        visited.add(tuple(head1))
        visited.add(tuple(head2))

        i += 2
        #print(adjacents)
        print(head1, head2)
        
    print(len(visited)  )
    # print(adjacents)
    # head1 = []
    # head2 = []
    # for key, value in adjacents.items():
    #     if value["val"] != '.':
    #         if head1:
    #             head2 = [key, value]
    #         else:
    #             head1 = [key, value]

    # print(head1, head2)

    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            c = matrix[y][x]
            if c == ".":
                print(colored(c, 'red'), end="")
            elif tuple([c, x, y]) in visited:    
                print(colored(c, 'green'), end="")
            else:
                print(c, end="")
        print("")

    ct = 0
    for y, row in enumerate(lines):
        inn = False
        for x, col in enumerate(row):
            c = matrix[y][x]
            if tuple([c, x, y]) not in visited:
                v = ""
                for i in range(0, x):
                    if tuple([matrix[y][i], i, y]) in visited:
                        v += matrix[y][i]
                #v = row[:x]

                counts = v.count("|") + v.count("J") + v.count("L") + v.count("S")
                if counts % 2 == 1:
                    print(row[:x])
                    print(v, counts)
                    ct += 1
                    #exit()
            # if matrix[y][x]:
            #     if matrix[y][x] in "|JL" or (G[i][j]=="S" and Svalid): inn = not inn
            # else:
            #     ct += inn
    print(ct)