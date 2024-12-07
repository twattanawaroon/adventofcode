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
    v = int(line.strip())*811589153
    seq.append((v, order))
    order += 1

n = len(seq)
for round in range(10):
    for i in range(n):
        d = find(seq, i)
        steps = seq[d][0] % (n-1)
        for t in range(steps):
            p = (d+t) % n
            q = (p+1) % n
            seq[p], seq[q] = seq[q], seq[p]
d = find(seq, 0, pos=0)
ansf = sum([seq[(d+t) % n][0] for t in range(1000, 3001, 1000)])
print(ansf)
