import sys

def incc(sb, pi, pj, pk):
    if (pi, pj, pk) not in sb:
        sb[(pi, pj, pk)] = 0
    sb[(pi, pj, pk)] += 1

def getc(sb, pi, pj, pk):
    if (pi, pj, pk) not in sb:
        return 0
    return sb[(pi, pj, pk)]

x = []
for line in sys.stdin:
    s = line.strip()
    x.append(s)

sa = set()
for i in range(len(x)):
    line = x[i]
    for j in range(len(line)):
        if line[j] == '#':
            sa.add((i, j, 0))

for tt in range(6):
    sb = dict()
    for pi, pj, pk in sa:
        for i in range(-1, 2):
            for j in range(-1, 2):
                for k in range(-1, 2):
                    if not (i == 0 and j == 0 and k == 0):
                        incc(sb, pi+i, pj+j, pk+k)
    sc = set()
    for pi, pj, pk in sb:
        if ((pi, pj, pk) in sa and 2 <= getc(sb, pi, pj, pk) <= 3) or ((pi, pj, pk) not in sa and getc(sb, pi, pj, pk) == 3):
            sc.add((pi, pj, pk))
    sa = sc

print(len(sa))