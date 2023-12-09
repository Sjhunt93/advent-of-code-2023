import re

def get_difs(num_list: list):
    results = []
    local = []
    assert len(num_list)
    for i in range(1, len(num_list)):
        local.append(num_list[i]-num_list[i-1])
    if local.count(0) == len(local):
        local.append(0)
        return [local]
    else:
        return get_difs(local) + [local]
    

def continue_right(structures):
    for s in range(1, len(structures)):
        carry = structures[s][-1] + structures[s-1][-1]
        structures[s].append(carry)

def continue_left(structures):
    for s in range(1, len(structures)):
        carry = structures[s][0] - structures[s-1][0]
        structures[s].insert(0, carry)

with open("data.txt") as f:
    lines = f.read().split("\n")
    results = 0
    for l in lines:
        numbers = [int(i) for i in re.findall("-?\d+", l)]
        print(numbers)
        structures = get_difs(numbers)
        structures.append(numbers)
        #print(structures)
        # for s in range(1, len(structures)):
        #     carry = structures[s][-1] + structures[s-1][-1]
        #     structures[s].append(carry)
        for s in range(1, len(structures)):
            carry = structures[s][0] - structures[s-1][0]
            structures[s].insert(0, carry)
        
        for s in structures:
            print(s)
            #results += carry
        #for s in structures:
        #results += structures[-1][-1]
        results += structures[-1][0]
        
    print(results)
        
        # for s in structures:
        #     print(s)
            
        