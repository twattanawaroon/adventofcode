import sys
import codelib as cl

a = []
b = []

for line in sys.stdin:
    s = line.strip().split()
    a.append(int(s[0]))
    b.append(int(s[1]))

freq = dict()
for item in b:
    if item not in freq:
        freq[item] = 0
    freq[item] += 1

ans = 0
for item in a:
    if item in freq:
        ans += item * freq[item]

print(ans)
