import re

card_dir = {}



def get_winnings(num, card, depth=0):
    nexts = []

    c = 1
    for i in card["inputs"]:
        if i in card["wins"]:
            nexts.append(c+num)
            c += 1
            
    s = len(nexts)
    for n in nexts:
        s += get_winnings(n, card_dir[n], depth+1)
    if not depth:
        return s+1
    else:
        return s
    

with open("data.txt") as f:

    lines = f.read().split("\n")
    sum = 0
    for l in lines:
        print(l)
        wins, inputs = l.split(":")[1].split("|")
        card = int(l.split("Card ")[1].split(":")[0])
        wins = re.findall("\d+", wins)
        inputs = re.findall("\d+", inputs)
        card_dir[card] = {
            "wins" : wins,
            "inputs" : inputs
        }
    
    res = 0
    for i, l in enumerate(lines):
        card = int(l.split("Card ")[1].split(":")[0])
        print(i)
        res += get_winnings(card, card_dir[card])
        
    print(res)