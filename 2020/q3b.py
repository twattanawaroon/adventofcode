import sys
pos = [(0, True)]*5
shift = [1,3,5,7,0.5]
count = [0]*5
for line in sys.stdin:
    s = line.strip()
    for i in range(5):
        p, q = pos[i]
        if s[p] == '#' and q:
            count[i] += 1
        if shift[i] == 0.5:
            if not q:
                pos[i] = (p, True)
            else:
                pos[i] = ((p+1)%len(s), False)
        else:
            pos[i] = ((p+shift[i])%len(s), True)
ans = 1
for c in count:
    ans *= c
print(ans)
