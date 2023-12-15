#data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

with open("data.txt") as f:
    data = f.read()

res = 0
for item in data.split(","):
    value = 0
    
    for c in item:
        value  = ((value + ord(c)) * 17) % 256
    print(value)
    res += value

print(res)
        