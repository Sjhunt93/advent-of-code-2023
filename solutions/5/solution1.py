import re

with open("data.txt") as f:
    items = f.read().split("\n\n")
    # for i in items:
    #     print(i, "\n")

    
    seeds = re.findall("\d+", items[0]) 
    print(seeds)
    steps = []
    for conversion in items[1:]:
        maps = conversion.split("\n")
        
        key = maps[0].split(" ")[0]
        #step = {key : []}
        print(key)
        choices = []
        for range in maps[1:]:
            source, destination, length = re.findall("\d+", range)
            print("--", source, destination, length)
            #step[key].append({"src" : source, "des" : destination, "len" : length})
            #choices.append({"src" : source, "des" : destination, "len" : length})
            choices.append([int(source), int(destination), int(length)])

        steps.append(choices)
    
    
    outputs = []
    for s in seeds:
        seed = int(s)
        for step in steps:
            print(step)
            for choice in step:
                #print(choice)
                if choice[1] <= seed < choice[1]+choice[2]:
                    dif = seed - choice[1]
                    output = choice[0]+dif
                    seed = output
                    break
            print(seed)
        outputs.append(seed)
    
    print(min(outputs), " --> ", outputs)
                

