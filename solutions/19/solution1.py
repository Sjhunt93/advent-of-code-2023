
from dataclasses import dataclass
from copy import deepcopy
import re
import operator
import functools

class Part():
    def __init__(self, line):
        self.x, self.m, self.a, self.s = re.findall("\d+", line)
        self.data = [int(i) for i in re.findall("\d+", line)]
    def get_sum(self):
        return sum(self.data)
    def get_val(self, key):
        return getattr(self, key)

class Rule():
    def __init__(self, line) -> None:
        self.rules = line[:-1].split(",")
        
    def evaluate(self, part):
        x, m, a, s = part.data
        for r in self.rules:
            if ':' in r:
                check, destination = r.split(":")
                if eval(check):
                    return destination
            else:
                return r


def evaluation_loop(ranges, token):
    if token == 'A':
        #a = functools.reduce(operator.mul, [len(value) for key, value in ranges.items()], 1)
        a = len(ranges['x']) * len(ranges["m"]) * len(ranges["a"]) * len(ranges["s"])
        #print(a, ranges)
        return a
    if token == 'R':
        return 0
    rule = workflows[token]
    count = 0
    for r in rule.rules:
        if ':' in r:
            check, destination = r.split(":")
            if '<' in r:
                lhs, rhs = check.split("<")
                
                branch_true = range(ranges[lhs].start, int(rhs))
                branch_false = range(int(rhs), ranges[lhs].stop)
                range_true = deepcopy(ranges)
                range_true[lhs] = branch_true
                
                ranges[lhs] = branch_false
                
                count += evaluation_loop(range_true, destination)
            elif '>' in r:
                lhs, rhs = check.split(">")
                
                branch_true = range(int(rhs)+1, ranges[lhs].stop)
                branch_false = range(ranges[lhs].start, int(rhs)+1)
                range_true = deepcopy(ranges)
                range_true[lhs] = branch_true
                
                ranges[lhs] = branch_false
                
                count += evaluation_loop(range_true, destination)
        else:
            count += evaluation_loop(ranges, r)

    return count

workflows = {}


with open("data.txt") as f:
    rules, data = f.read().split("\n\n")
    
    for r in rules.split("\n"):
        a, b = r.split("{")
        workflows[a] = Rule(b)

    valids = []
    for p in data.split("\n"):
        part = Part(p)
        res = 'in'
        while res not in ["R", "A"]:
            res = workflows[res].evaluate(part)
        if res == 'A':
            valids.append(part)

    # part 1:
    r = sum([v.get_sum() for v in valids])
    print(r)

    ranges = {
        "x" : range(1, 4001),
        "m" : range(1, 4001),
        "a" : range(1, 4001),
        "s" : range(1, 4001)
    }
    result = evaluation_loop(ranges, "in")
    # part 2
    print(result, " --> ")