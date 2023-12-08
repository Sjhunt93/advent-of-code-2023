import re

def process_seed(seed, steps):
    for step in steps:
        
        for choice in step:
            #print(choice)
            if choice[1] <= seed < choice[1]+choice[2]:
                dif = seed - choice[1]
                output = choice[0]+dif
                seed = output
                break
    return seed

with open("data.txt") as f:
    items = f.read().split("\n\n")
    # for i in items:
    #     print(i, "\n")

    
    seeds = re.findall("\d+", items[0]) 

    # exit()
    steps = []
    for conversion in items[1:]:
        maps = conversion.split("\n")
        
        key = maps[0].split(" ")[0]
        #step = {key : []}
        print(key)
        choices = []
        for r in maps[1:]:
            source, destination, length = re.findall("\d+", r)
            print("--", source, destination, length)
            #step[key].append({"src" : source, "des" : destination, "len" : length})
            #choices.append({"src" : source, "des" : destination, "len" : length})
            choices.append([int(source), int(destination), int(length)])

        steps.append(choices)
    
    print(steps)
    print([int(s) for s in seeds])
    print("\\n\n\nn")
    for step in steps:
        items = []
        for choice in step:
            [items.append(c) for c in choice]
        print(items)

    exit()

    min_found = 2540650
    #print(seeds, len(seeds))
    jump = 1000
    for i in range(8, len(seeds), 2):
        
        a, b = seeds[i:i+2]
        print(a, b)
        j = int(a)+int(b)
        if i != 8:
            continue
        #while j < int(a)+int(b):
        while j >= int(a):
        #for j in range(int(a), int(a)+int(b), jump):
            #print(j)
            #r = process_seed(j, steps)
            
            seed = j
            for step in steps:
        
                for choice in step:
                    #print(choice)
                    if choice[1] <= seed < choice[1]+choice[2]:
                        dif = seed - choice[1]
                        output = choice[0]+dif
                        seed = output
                        break


            if j % 100000 == 0:
                print(j, (int(a)+int(b))-j)
                
            if seed < min_found:
                min_found = seed
                jump = 10
                print("*******",min_found)

            j -= jump
        print("MIN for stack", i, min_found)

    # print(all_seeds)
    # print(seeds)
    print(min_found)