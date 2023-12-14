#from termcolor import colored
import itertools


def to_matrix(lines):
    items = []
    for l in lines:
        items.append([i for i in l])
    return items

def check_horizontal(matrix, ignore=-1):
    
    for i in range(1, len(matrix)):
        if i == ignore:
            continue
        reflections = 0    
        a = i-1
        b = i
        while True:    
            if a >= 0 and b < len(matrix) and matrix[a] == matrix[b]:
                reflections += 2
                a -= 1
                b += 1
            else:
                # has either a or b hit the edge
                if reflections >= 2 and (a < 0 or b >= len(matrix)): 
                    return i
                else:
                    break

    return 0


def rotate_matrix(matrix):

    new_matrix = []

    for col in range(len(matrix[0])):
        new_row = []
        for row in range(len(matrix)): 
            new_row.append(matrix[row][col])
        new_matrix.append(new_row)

    return new_matrix

def toggle(matrix, i):
    y = int(i / len(matrix[0]))
    x = i % len(matrix[0])
    
    if matrix[y][x] == '#':
        matrix[y][x] = '.'
    else:
        matrix[y][x] = '#'

# HELPER
#print(hscore, vscore)
# for y, row in enumerate(matrix):
#     print(row)
#     for x, col in enumerate(row):
#         c = matrix[y][x]

with open("data.txt") as f:

    mirrors = f.read().split("\n\n")
    r = 0
    part_2 = []
    for i, m in enumerate(mirrors):
        print(m)
        matrix = to_matrix(m.split("\n"))
        hscore = check_horizontal(matrix) * 100
        vscore = check_horizontal(rotate_matrix(matrix))
        assert hscore == 0 or vscore == 0
        r += hscore + vscore

        part_2.append([matrix, hscore, vscore])
    print(r)
    
    # --------------------- part 2 ---------------------
    res = 0
    for mirror in part_2:
        matrix, h_old, n_old = mirror
        i = 0
        print("###", h_old, n_old)
        
        while True:
            toggle(matrix, i)
            hscore = check_horizontal(matrix, int(h_old/100) if h_old else -1 ) * 100
            vscore = check_horizontal(rotate_matrix(matrix), n_old if n_old else -1)
            toggle(matrix, i)
            print(i, hscore, vscore)
            if [hscore, vscore] != [h_old, n_old] and hscore + vscore != 0:
                print("new score",[hscore, vscore] , " old...", [h_old, n_old])
                if hscore == h_old:
                    score = vscore
                elif vscore == n_old:
                    score = hscore
                else:
                    score = hscore + vscore
                
                print(score)
                res += score
                break
            i += 1
            if i >= len(matrix) * len(matrix[0]):
                break
        
    
    print(res)

            

    