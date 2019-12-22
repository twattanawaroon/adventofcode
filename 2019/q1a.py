import sys
count = 0
for line in sys.stdin:
    count += (int(line))//3-2
print(count)