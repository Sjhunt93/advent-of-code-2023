import re
import itertools
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

A = (0,0)
B = (10, 10)
# C = (0, 10)
# D = (10, 0)

C = (0,0)
D = (10, 10)

#print(line_intersection((A, B), (C, D)))

# MIN = 7
# MAX = 27

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

    # def get_region_leave(self, xmin, ymin, xmax, ymax):
    #     if self.xv < 0: # moving away
    #         d = self.x - xmin

    #     #xend = 
        
    #     y = x - 2
    
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

    # A, B = hailstones[0].get_max_points(7, 27)
    # C, D = hailstones[1].get_max_points(7, 27)
    # print(line_intersection((A, B), (C, D)))

    pairs = itertools.combinations(hailstones, 2)
    print("\n\n\n\n")
    intersections = 0
    crosses = set()
    for p in pairs:
        #print(vars(p[0]), vars(p[1]))
        #print(p[0].i, p[1].i)
        
        plot1, plot2 = p
        print(plot1.line)
        print(plot2.line)
        A, B = plot1.plot_line(MIN, MAX)
        C, D = plot2.plot_line(MIN, MAX)
        print(A, B,C ,D)
        result = line_intersection((A, B), (C, D))
        if result:
            print("-->", result)
            x, y = result
            if MIN <= x <= MAX and MIN <= y <= MAX:
                if min(A[0], B[0]) <= x <= max(A[0], B[0]):
                    if min(A[1], B[1]) <= y <= max(A[1], B[1]):
                        if min(C[0], D[0]) <= x <= max(C[0], D[0]):
                            if min(C[1], D[1]) <= y <= max(C[1], D[1]):
                    
                #if plot1.i not in crosses and plot2.i not in crosses:
                                print("yes")
                                intersections += 1
                                
                # else:
                #     print("already in results")
            #     print(result)
            
        else:
            print(" X")
        print("\n")

    print(intersections, len(crosses))
