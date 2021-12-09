import sys

for line in sys.stdin:
    x = list(map(int,line.strip().split(',')))
    x.sort()
    med = x[len(x)//2]
    print(sum([abs(med-c) for c in x]))
