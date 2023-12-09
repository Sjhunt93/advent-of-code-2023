import re

def get_difs(num_list: list):
    
    local = []

    for i in range(1, len(num_list)):
        local.append(num_list[i]-num_list[i-1])
    if local.count(0) == len(local):
        return [local]
    else:
        return get_difs(local) + [local]
    

def continue_right(structures):
    for s in range(1, len(structures)):
        carry = structures[s][-1] + structures[s-1][-1]
        structures[s].append(carry)
    return structures[-1][-1]

def continue_left(structures):
    for s in range(1, len(structures)):
        carry = structures[s][0] - structures[s-1][0]
        structures[s].insert(0, carry)
    return structures[-1][0]

with open("data.txt") as f:
    lines = f.read().split("\n")
    results = 0
    for l in lines:
        numbers = [int(i) for i in re.findall("-?\d+", l)]
        print(numbers)
        structures = get_difs(numbers)
        structures.append(numbers)
        # part 1
        #results += continue_left(structures)
        # part 2
        results += continue_right(structures)

        
    print(results)
        
            
        