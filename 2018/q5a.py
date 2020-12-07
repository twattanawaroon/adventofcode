import sys

s = [line.strip() for line in sys.stdin]
x = []
for c in s[0]:
    if len(x) == 0 or abs(ord(x[-1])-ord(c)) != 32:
        x.append(c)
    else:
        x.pop()
print(len(x))