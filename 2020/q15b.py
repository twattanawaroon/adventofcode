import sys

for line in sys.stdin:
    inp = list(map(int, line.strip().split(',')))
    last = dict()
    lnum = None
    for i in range(30000000):
        if i < len(inp):
            num = inp[i]
        else:
            if lnum not in last:
                num = 0
            else:
                num = (i-1)-last[lnum]
        last[lnum] = i-1
        lnum = num
    print(num)
