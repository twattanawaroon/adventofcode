import sys

def process(text):
    v = text.strip().split()
    return int(v[0]), int(v[6])

inp = [process(line) for line in sys.stdin]
for p, n in inp:
    score = [0]*p
    ans = 0
    pos = 0
    cur = [0]
    for i in range(1, n+1):
        if i%23 == 0:
            pos = (pos+len(cur)-7)%len(cur)
            score[(i-1)%p] += cur[pos]+i
            cur = cur[:pos]+cur[pos+1:]
            pos %= len(cur)
        else:
            pos = (pos+1)%len(cur)
            cur = cur[:pos+1]+[i]+cur[pos+1:]
            pos += 1
    print(max(score))