import re
import itertools
import math


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       #raise Exception('lines do not intersect')
        return None

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y

MIN = 200000000000000
MAX = 400000000000000

class Hail():
    def __init__(self, i, x, y, z, xv, yv, zv, line) -> None:
        self.i = i
        self.x = x
        self.y = y
        self.z = z
        self.xv = xv
        self.yv = yv
        self.zv = zv
        self.line = line


    
    def solve_y_mx_c(self):
        x2 = self.x + self.xv
        y2 = self.y + self.yv

        m = (y2-self.y) / (x2-self.x)
        c = self.y - m * self.x

        print(f"y = {m}x + {c}")
        self.ycalc = lambda x: m*x + c

    def get_max_points(self, xmin, xmax):
        ym = self.ycalc(xmin)
        ymax = self.ycalc(xmax)

        return (xmin, ym), (xmax, ymax)

    def plot_line(self, xmin, xmax):
        ym = self.ycalc(xmin)
        ymax = self.ycalc(xmax)
        if self.xv < 0: # negative
            return (self.x, self.y), (xmin, ym)
        else:
            return (self.x, self.y), (xmax, ymax)
            



hailstones = []

with open("data.txt") as f:

    lines = f.read().split("\n")
    cid = 0
    for l in lines:
        a,b,c,d,e,f = [int(i) for i in re.findall("-?\d+", l)]
        hailstones.append(Hail(cid, a,b,c,d,e,f, l))
        cid += 1

    for h in hailstones:
        h.solve_y_mx_c()


    mindis = 10000000000000
    minx = mindis
    miny = mindis
    minz = mindis
    best = None
    for i in range(0, len(hailstones)):
        for j in range(i, len(hailstones)):
            if i == j:
                continue
            
            x = (hailstones[i].x - hailstones[j].x)
            y = (hailstones[i].y - hailstones[j].y)
            z = (hailstones[i].z - hailstones[j].z)
            minx = min(abs(x), minx)
            miny = min(abs(y), miny)
            minz = min(abs(z), minz)
            distance = math.sqrt((x ** 2) + (y ** 2) + (z ** 2))
            print(distance)
            if distance < mindis:
                mindis = distance
                best = (hailstones[i], hailstones[j])
    
    print(vars(best[0]))
    print(vars(best[1]))
    print(minx, miny, minz)

