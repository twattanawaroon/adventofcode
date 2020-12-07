import sys

edgestr = [line.strip() for line in sys.stdin]
edges = {}
indeg = {}
zeroes = []
for i in range(26):
    c = chr(ord('A')+i)
    edges[c] = []
    indeg[c] = 0
for e in edgestr:
    edgespl = e.split()
    p = edgespl[1]
    q = edgespl[7]
    edges[p].append(q)
    indeg[q] += 1
for i in range(26):
    c = chr(ord('A')+i)
    if indeg[c] == 0:
        zeroes.append(c)
workdone = 0
time = 0
workers = [0]*5
working = [None]*5
while workdone < 26:
    for i in range(5):
        if working[i] is not None:
            workers[i] -= 1
            if workers[i] <= 0:
                workdone += 1
                for q in edges[working[i]]:
                    indeg[q] -= 1
                    if indeg[q] == 0:
                        zeroes.append(q)
                working[i] = None
    for i in range(5):
        if working[i] is None and len(zeroes) > 0:
            zeroes.sort()
            zeroes = zeroes[::-1]
            c = zeroes.pop()
            working[i] = c
            workers[i] = ord(c)-ord('A')+61
    time += 1
print(time-1)