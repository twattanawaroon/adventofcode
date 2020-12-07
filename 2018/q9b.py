import sys

def process(text):
    v = text.strip().split()
    return int(v[0]), int(v[6])

inp = [process(line) for line in sys.stdin]
for p, n in inp:
    score = [0]*p
    mprev = [0]
    mnext = [0]
    pos = 0
    cur = [0]
    for i in range(1, n*100+1):
        if i%23 == 0:
            for c in range(7):
                pos = mprev[pos]
            score[(i-1)%p] += cur[pos]+i
            n1 = mprev[pos]
            n2 = mnext[pos]
            mnext[n1] = n2
            mprev[n2] = n1
            pos = n2
        else:
            n1 = mnext[pos]
            n2 = mnext[n1]
            n0 = len(cur)
            mprev.append(n1)
            mnext.append(n2)
            cur.append(i)
            mnext[n1] = n0
            mprev[n2] = n0
            pos = n0
    print(max(score))