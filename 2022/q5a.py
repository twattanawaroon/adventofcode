import sys
import codelib as cl
from aocd import submit

N = 9
count = 0
mode = False
s = []
for i in range(N):
    s.append([])
for line in sys.stdin:
    t = line
    if not mode:
        if len(t) == 1:
            for i in range(N):
                s[i] = s[i][::-1]
            mode = True
        else:
            for i in range(N):
                if i*4+1 < len(t) and t[i*4] == '[':
                    s[i].append(t[i*4+1])
    elif len(t) > 1:
        tt = t.split()
        q = int(tt[1])
        a = int(tt[3])-1
        b = int(tt[5])-1
        for i in range(q):
            c = s[a].pop()
            s[b].append(c)
ansf = ''.join([s[i][-1] for i in range(N)])
#print(ansf)

submit(ansf, part="a", day=5, year=2022)