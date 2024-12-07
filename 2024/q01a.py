import sys
import codelib as cl

a = []
b = []

for line in sys.stdin:
    s = line.strip().split()
    a.append(int(s[0]))
    b.append(int(s[1]))

a.sort()
b.sort()

ans = 0
for i in range(len(a)):
    ans += abs(a[i]-b[i])

print(ans)
