import sys

x = []
count = 0
for line in sys.stdin:
    x = line.strip().split('|')
    b = x[1].strip().split()
    for item in b:
        if len(item) in [2,3,4,7]:
            count += 1

print(count)
