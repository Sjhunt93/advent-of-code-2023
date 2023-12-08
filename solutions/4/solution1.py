import re
with open("data.txt") as f:

    lines = f.read().split("\n")
    sum = 0
    for l in lines:
        print(l)
        wins, inputs = l.split(":")[1].split("|")

        wins = re.findall("\d+", wins)
        score = 0
        for i in re.findall("\d+", inputs):
            if i in wins:
                if not score:
                    score = 1
                else:
                    score = score * 2
        print(score)

        sum += score
    print(sum)