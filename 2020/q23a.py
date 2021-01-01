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
    s = line.strip()
    nx = dict()
    for i in range(len(s)):
        nx[int(s[i])] = int(s[(i+1)%len(s)])
    curr = int(s[0])
    for i in range(100):
        process(nx, curr, len(s))
        curr = nx[curr]
    ans = []
    curr = nx[1]
    while curr != 1:
        ans.append(curr)
        curr = nx[curr]
    print(''.join(list(map(str,ans))))
