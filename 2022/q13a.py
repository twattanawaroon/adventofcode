import sys
import codelib as cl
import ast


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


a = None
b = None
cnt = 0
ansf = 0
for line in sys.stdin:
    s = line.strip()
    if len(s) > 0:
        t = ast.literal_eval(s)
        if a is None:
            a = t
        elif b is None:
            b = t
    if a is not None and b is not None:
        cnt += 1
        if compare(a, b) <= 0:
            ansf += cnt
        a = None
        b = None

print(ansf)
