import sys
import codelib as cl

s = set()
folds = None

for line in sys.stdin:
    x = line.strip()
    if len(x) > 0 and x[0] == 'f':
        it = x.split()[2]
        it1, it2 = it.split('=')
        if folds is None:
            folds = [(it1, int(it2))]
    elif len(x) > 0:
        s.add(tuple(map(int, x.split(','))))

for fd, fv in folds:
    s2 = set()
    for item in s:
        x, y = item
        if fd == 'x' and x >= fv:
            s2.add((2*fv-x, y))
        elif fd == 'y' and y >= fv:
            s2.add((x, 2*fv-y))
        else:
            s2.add((x, y))
    s = s2

print(len(s))
