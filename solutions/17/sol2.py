
import heapq

moves = {
    "^" : [0, -1],
    "v" : [0, 1],
    "<" : [-1, 0],
    ">" : [1, 0]
}
opposite = {"<": ">", ">": "<", "v": "^", "^": "v"}


def astartv2(maze, start, end):
    start = (0,0)
    end = (len(maze[0])-1, len(maze)-1)

    to_visit = [(0, ">", start), (0, "v", start)]
    visited = set()

    while to_visit:
        current_lava, current_dir, current_pos = heapq.heappop(to_visit)
        if (current_pos, current_dir) in visited:
            continue

        visited.add((current_pos, current_dir))
        for d, move in moves.items():
            x = current_pos[0] + move[0]
            y = current_pos[1] + move[1]
            new_pos = (x, y)
            # out of bounds
            if x < 0 or x >= len(maze[0]) or y < 0 or y >= len(maze):
                continue
            if d == current_dir[-1] and len(current_dir) == 10: # has reached 3 steps..
                continue
            if d != current_dir[-1] and len(current_dir) < 4:
                continue
            if current_dir[-1] == opposite[d]: # 180 degree turn
                continue

            if d == current_dir[-1]:
                new_direction = current_dir + d
            else:
                new_direction = d
            
            if (new_pos, new_direction) in visited:
                continue
            lava = int(maze[y][x])
            if new_pos == end and len(new_direction) >= 4:
                return current_lava + lava
            
            #print(current_lava + lava, new_direction, new_pos)
            heapq.heappush(to_visit, (current_lava + lava, new_direction, new_pos))



                



def to_matrix(lines):
    items = []
    for l in lines:
        #print(l)
        items.append([i for i in l])
    return items

# HELPER
#print(hscore, vscore)
# for y, row in enumerate(matrix):
#     print(row)
#     for x, col in enumerate(row):
#         c = matrix[y][x]


with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)

    start = (0, 0)
    end = (len(matrix[0])-1, len(matrix)-1)

    paths = astartv2(matrix, start, end)
    
    print(paths)
    
    # for path in paths:
    #     cost = 0
    #     for p in path:
    #         cost += int(matrix[p[1]][p[0]])
    #         #matrix[p[1]][p[0]] = "#"
    #     print(path, cost)

    # # for r in matrix:
    # #     print(''.join([i for i in r]))
    # # print("\n")

    