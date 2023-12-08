
nums = [str(i) for i in range(0, 10)]

def to_matrix(lines):
    items = []
    for l in lines:
        items.append([i for i in l])
    return items

def check_adjanecy(xi, yi, matrix):

    print(matrix[yi][xi])
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



with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    print(matrix)
    stack = []
    score = 0
    for y, row in enumerate(lines):
        for x, col in enumerate(row):
            c = matrix[y][x]
            #print(c, stack)
            if x == 0 and stack:
                # do routines..
                pass

            if c in nums and x != len(row)-1:
                stack.append(c)
            elif stack:
                if c in nums:
                    stack.append(c)
                #if c not in nums or x == len(row)-1:
                print("checking...", stack)
                matches = False
                for i, val in enumerate(stack):
                    if check_adjanecy(x-i-1, y, matrix):
                        matches = True
                if matches:
                    num = int(''.join([i for i in stack]))
                    print(num)
                    score += num
                stack = []

            # else:
            #     stack.append(c)
    
    print(score)
