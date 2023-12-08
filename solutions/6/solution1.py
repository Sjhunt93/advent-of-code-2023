import re

with open("data.txt") as f:
#with open("data2.txt") as f:
    time, distance = f.read().split("\n")
    # for i in items:
    #     print(i, "\n")

    
    times = [int(i) for i in re.findall("\d+", time)]
    distances = [int(i) for i in re.findall("\d+", distance)]
    print(times, distances)

    result = 1
    for t, d in zip(times, distances):
        print(t, d)
        record = 0
        for i in range(t):
            velocity = i
            distance = velocity * (t-i)
            #print("amount", velocity, "=>", distance)
            if i % 1000:
                print("amount", velocity, "=>", distance)
            if distance > d:
                record += 1
        print(record)
        result *= record
        break
    print(result)