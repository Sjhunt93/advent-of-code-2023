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
        counts = {
            "red" : [],
            "blue" : [],
            "green" : []
        }
        
        for g in games:
            
            cubes = g.split(",")
            print(cubes)
            for c in cubes:
                num, col = c.strip().split(" ")
                print(num, col, end=" ")
                counts[col].append(int(num))
        
        c = 1
        for key, val in counts.items():
            c *= max(val)
        
        s += c
    print("LIMITS", s)