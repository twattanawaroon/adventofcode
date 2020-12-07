import sys
OFFSET = 300
MX = 1000

def process(text):
    x, y = map(int, text.strip().split(','))
    return (x+OFFSET, y+OFFSET)

points = [process(line) for line in sys.stdin]
ans = 0
for i in range(MX):
    for j in range(MX):
        dist = sum([abs(x-i)+abs(y-j) for x, y in points])
        if dist < 10000:
            ans += 1
print(ans)