import sys

s = [line.strip() for line in sys.stdin]
bestlen = None
for i in range(26):
    x = []
    for c in s[0]:
        if ord(c)-i == ord('A') or ord(c)-i == ord('a'):
            pass
        elif len(x) == 0 or abs(ord(x[-1])-ord(c)) != 32:
            x.append(c)
        else:
            x.pop()
    if bestlen is None or len(x) < bestlen:
        bestlen = len(x)
print(bestlen)