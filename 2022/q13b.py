import sys
import codelib as cl
import ast
import functools


def compare(a, b):
    if isinstance(a, list) and isinstance(b, list):
        for i in range(min(len(a), len(b))):
            c = compare(a[i], b[i])
            if c != 0:
                return c
        return len(a)-len(b)
    elif isinstance(a, list):
        return compare(a, [b])
    elif isinstance(b, list):
        return compare([a], b)
    else:
        return a-b


x = []
da = [[2]]
db = [[6]]
ansf = 1
x.append(da)
x.append(db)
for line in sys.stdin:
    s = line.strip()
    if len(s) > 0:
        t = ast.literal_eval(s)
        x.append(t)
x.sort(key=functools.cmp_to_key(compare))
for i in range(len(x)):
    if x[i] == da or x[i] == db:
        ansf *= i+1

print(ansf)
