
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

def are_in_distance(number, x, y):
    ydif = abs(number["row"]-y)
    for xs in number["xs"]:
        xdif = abs(xs-x)
        if xdif <= 1 and ydif <= 1:
            return True
    
    return False



with open("data.txt") as f:

    lines = f.read().split("\n")
    matrix = to_matrix(lines)
    print(matrix)
    stack = []
    score = 0
    symbols = []
    numbers = []
    for y, row in enumerate(lines):
        clear_stack = False
        for x, col in enumerate(row):
            c = matrix[y][x]
            
            if c in nums:
                stack.append([c, x])
            else:
                symbols.append(
                    {"pos" : [x, y], "sym" : c}
                )
                print(c)
                if stack:
                    clear_stack = True
            if x == len(row)-1 and stack:
                print("hit end", x)
                clear_stack = True
                
            
            if clear_stack and stack:
                # find gears first
                matches = False
                for i, val in enumerate(stack):
                    if check_adjanecy(x-i-1, y, matrix):
                        matches = True
                if matches:
                    print("clearing...", stack)
                    num = int(''.join([i[0] for i in stack]))
                    #numbers.append({"row" : y, "xs" : [stack[0][1], stack[-1][1]], "num" : num})
                    numbers.append({"row" : y, "xs" : [i[1] for i in stack], "num" : num})
                stack = []
                clear_stack = False
                

    res = 0
    for s in symbols:
        if s["sym"] == "*":
            d = 0
            hits = []
            for n in numbers:
                if are_in_distance(n, s["pos"][0], s["pos"][1]):
                    hits.append(n)
            if len(hits) == 2:
                #print(hits[0]["num"] * hits[1]["num"])
                res += (hits[0]["num"] * hits[1]["num"])
            else:
                print("miss..", s)
    print("r", res)
    