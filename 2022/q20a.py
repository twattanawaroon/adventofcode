import sys
import codelib as cl


def find(seq, v, pos=1):
    for i in range(len(seq)):
        if seq[i][pos] == v:
            return i


seq = []
val = dict()
order = 0
for line in sys.stdin:
    v = int(line.strip())
    seq.append((v, order))
    order += 1

n = len(seq)
for i in range(n):
    d = find(seq, i)
    steps = seq[d][0] % (n-1)
    for t in range(steps):
        p = (d+t) % n
        q = (p+1) % n
        r = seq[p]
        seq[p] = seq[q]
        seq[q] = r
d = find(seq, 0, pos=0)
ansf = sum([seq[(d+t) % n][0] for t in range(1000, 3001, 1000)])
print(ansf)
