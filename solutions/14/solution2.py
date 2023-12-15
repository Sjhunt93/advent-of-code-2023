#from termcolor import colored
import itertools
from copy import deepcopy

def to_matrix(lines):
    items = []
    for l in lines:
        items.append([i for i in l])
    return items



def move_rock(matrix, x, y, direction):
    moves = {
        "N" : [0, -1],
        "S" : [0, 1],
        "E" : [-1, 0],
        "W" : [1, 0]
    }

    if matrix[y][x] != 'O':
        return

    matrix[y][x] = '.'
    
    while y >= 0 and y < len(matrix) and x >= 0 and x < len(matrix[0]) and matrix[y][x] not in ['#', 'O']:
        mx, my = moves[direction]
        x += mx
        y += my
    
    mx, my = moves[direction]
    matrix[y + my * -1][x + mx*-1] = 'O'




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
inset = 0
with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    


    #for i in "NWSE":
    Y_SIZE = len(matrix)
    X_SIZE = len(matrix[0])
    scores = []
    for i in range(0, 1000):
        
        for row in range(0, len(matrix)):
            for x in range(0, len(matrix[0])):
                move_rock(matrix, x, row, 'N')

        # for row in range(0, len(matrix)):
        #     print(''.join(matrix[row]))
        # print("\n")

        for x in range(0, len(matrix[0])):
            for row in range(0, len(matrix)):
                move_rock(matrix, x, row, 'E')
        # for row in range(0, len(matrix)):
        #     print(''.join(matrix[row]))
        # print("\n")

        for row in range(0, len(matrix)):
            for x in range(0, len(matrix[0])):
                move_rock(matrix, x, (Y_SIZE-1)-row, 'S')
        # for row in range(0, len(matrix)):
        #     print(''.join(matrix[row]))
        # print("\n")

        for x in range(0, len(matrix[0])):
            for row in range(0, len(matrix)):
                move_rock(matrix, (X_SIZE-1)-x, row, 'W')
        # for row in range(0, len(matrix)):
        #     print(''.join(matrix[row]))
        # print("\n")
    
        r = len(matrix)
        score = 0
        for row in matrix:
            score += (row.count('O') * r)
            r -= 1

        print(i, score)
        if scores.count([score, matrix]) == 2:
            print("\t", "duplicate")
            z = 0
            start = 0
            repeats = 0
            for i, old in enumerate(scores):
                if old == [score, matrix]:
                    if start == 0:
                        start = i
                    else:
                        repeats = i-start
            print("starts", start, " repeats ", repeats)
            a = (1000000000-start) % repeats
            print(scores[a+start-1][0])
            exit()

        scores.append([score, deepcopy(matrix)])
        
    
    #score = [row.count('O') * r for row in matrix]
        

    #print(score)
    
