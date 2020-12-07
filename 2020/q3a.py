import sys
count = 0
pos = 0
for line in sys.stdin:
    s = line.strip()
    if s[pos] == '#':
         count += 1
    pos = (pos+3)%len(s)
print(count)
