import sys

t = None
x = []
for line in sys.stdin:
    s = line.strip()
    if t is None:
        t = int(s)
    else:
        for item in s.split(','):
            if item != 'x':
                x.append(int(item))

mint, bus = min([(((t+c-1)//c)*c, c) for c in x])
print(bus*(mint-t))
