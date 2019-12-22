import sys

def process(n):
    ans = 0
    while n > 0:
        n = max((n//3)-2, 0)
        ans += n
    return ans

count = 0
for line in sys.stdin:
    count += process(int(line))
print(count)