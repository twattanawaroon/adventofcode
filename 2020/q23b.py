import sys

def get_ih(nx, curr, cups, used):
    p = curr
    while True:
        p -= 1
        if p <= 0:
            p = cups
        if p not in used:
            return p

def process(nx, curr, cups):
    hd = nx[curr]
    tl = curr
    used = []
    for i in range(3):
        tl = nx[tl]
        used.append(tl)
    nx[curr] = nx[tl]
    ih = get_ih(nx, curr, cups, used)
    nx[tl] = nx[ih]
    nx[ih] = hd

for line in sys.stdin:
    cups = 1000000
    s = line.strip()
    nx = dict()
    for i in range(len(s)-1):
        nx[int(s[i])] = int(s[i+1])
    for i in range(len(s)+1, cups):
        nx[i] = i+1
    nx[int(s[-1])] = len(s)+1
    nx[cups] = int(s[0])
    curr = int(s[0])
    for i in range(10000000):
        process(nx, curr, cups)
        curr = nx[curr]
    print(nx[1] * nx[nx[1]])
