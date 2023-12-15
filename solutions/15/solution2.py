data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

with open("data.txt") as f:
    data = f.read()

big_map = {

}

def hash(val):
    value = 0
    for c in val:
        value  = ((value + ord(c)) * 17) % 256
    return value

def remove_label(labels, label):
    a = []
    for l in labels:
        if l[0] != label:
            a.append(l)
    return a
            
def replace_label(labels, label, lens):
    for l in labels:
        if l[0] == label:
            l[1] = lens
            return True
    return False

res = 0
for item in data.split(","):
    value = 0
    print(item)
    if '-' in item:
        label = item.split("-")[0]
        index = hash(label)
        if index in big_map:
            #if label in big_map[index]:
                #big_map[index].remove(label)
            big_map[index] = remove_label(big_map[index], label)

    if '=' in item:
        label, lens = item.split("=")
        index = hash(label)
        if index in big_map:
            if not replace_label(big_map[index], label, lens):
                big_map[index].append([label, lens])
        else:
            big_map[index] = [[label, lens]]

r = 0
for key, value in big_map.items():
    print(key, value)
    c = 0
    for i, v in enumerate(value):
        c += (((key+1) * (i+1)) * int(v[1]))
    print(c)
    r += c
    # for c in item:
    #     value  = ((value + ord(c)) * 17) % 256
    # print(value)
    # res += value

print(r)
        