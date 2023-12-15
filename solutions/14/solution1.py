#from termcolor import colored
import itertools


def to_matrix(lines):
    items = []
    for l in lines:
        items.append([i for i in l])
    return items

def move_rock(matrix, x, y):
    if matrix[y][x] != 'O':
        return

    matrix[y][x] = '.'
    while y >= 0 and matrix[y][x] not in ['#', 'O']:
        y -= 1
    matrix[y+1][x] = 'O'

    


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

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    
    for row in range(0, len(matrix)):
        for x in range(0, len(matrix[0])):
            move_rock(matrix, x, row)
        #print(matrix[row])
    
    for row in range(0, len(matrix)):
        print(matrix[row])
    
    r = len(matrix)
    score = 0
    for row in matrix:
        score += (row.count('O') * r)
        r -= 1
    
    print(score)
    
