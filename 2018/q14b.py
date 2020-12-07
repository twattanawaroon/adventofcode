import sys

def process(text):
    return text.strip()

inps = [process(line) for line in sys.stdin]
for inp in inps:
    x = [3, 7]
    pos1 = 0
    pos2 = 1
    nc = 0
    found = False
    while not found:
        num = x[pos1]+x[pos2]
        if num >= 10:
            x.append(num//10)
            x.append(num%10)
        else:
            x.append(num)
        pos1 = (pos1+x[pos1]+1)%len(x)
        pos2 = (pos2+x[pos2]+1)%len(x)
        while nc+len(str(inp)) <= len(x):
            cand = ''.join(map(str, x[nc:nc+len(str(inp))]))
            if cand == inp:
                print(nc)
                found = True
                break
            nc += 1