limits = {
    "red" : 12,
    "green" : 13,
    "blue" : 14
}

with open("data.txt") as f:
    lines = f.read().split("\n")
    s = 0
    for l in lines:
        id, cubes = l.split(":")
        games = cubes.split(";")
        is_valid = True
        for g in games:
            cubes = g.split(",")
            print(cubes)
            for c in cubes:
                num, col = c.strip().split(" ")
                print(num, col, end=" ")
                if int(num) > limits[col]:
                    is_valid = False
        if is_valid:
            s += int(id.split("Game")[-1])
    print("LIMITS", s)