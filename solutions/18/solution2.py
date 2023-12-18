


def shoelace(vertices):
    #https://www.101computing.net/the-shoelace-algorithm/
    p1 = 0
    p2 = 0
    for i in range(0, len(vertices)-1):
        p1 += (vertices[i][0] * vertices[i+1][1])
        p2 += (vertices[i+1][0] * vertices[i][1])
    
    #cross over the last 2
    p1 += vertices[len(vertices)-1][0] * vertices[0][1]   
    p2 += vertices[0][0] * vertices[len(vertices)-1][1]   

    return abs(p1 - p2) // 2


with open("data.txt") as f:
    dig_instructions = f.read().split("\n")

    
    path = [(0,0)]
    

    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    perimeter = 0
    for ins in dig_instructions:
        dir, inc, col = ins.split(" ")
        hcode  = col.split("#")[1][:-1]
        dir = int(hcode[-1])
        x = int(hcode[:-1], 16)
        print(x, dir)
        
        perimeter += x
        #print(dir, inc, col)
        if dir == 0: # right
            path.append((path[-1][0] + x, path[-1][1]))
        elif dir == 1: # down
            path.append((path[-1][0], path[-1][1] + x))
        elif dir == 2: # left
            path.append((path[-1][0] - x, path[-1][1]))
        elif dir == 3: # down
            path.append((path[-1][0], path[-1][1] - x))
        
        max_x = max(max_x, path[-1][0])
        max_y = max(max_y, path[-1][1])
        min_x = min(min_x, path[-1][0])
        min_y = min(min_y, path[-1][1])
    for p in path:
        print(p)
    


    #path.reverse()
    
    area = shoelace(path)

    print("Polygon Vertices:")
    print("")
    print("Area = " + str(area) + "cm2")
    print(perimeter)
    print(int(area - perimeter / 2 + 1) + perimeter)

#    print(max_x, max_y)

    # dig_map = []
    # for i in range(abs(min_y) + max_y+3):
    #     dig_map.append(['.' for x in range(abs(min_x) + max_x+3)])

    # for p in path:
    #     y = abs(min_y)+p[1]+1
    #     x = abs(min_x)+p[0]+1
    #     assert x >=0
    #     assert y >= 0
    #     dig_map[y][x] = '#'

    
    
    # counts = 0
    # for row in dig_map:
        
    #     print(''.join([c for c in row]))
    #     counts += row.count("#") + row.count(".")
    
    # print(counts)

