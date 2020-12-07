import sys

def process(text):
    return int(text.strip())

inps = [process(line) for line in sys.stdin]
for inp in inps:
    x = [3, 7]
    pos1 = 0
    pos2 = 1
    while len(x) <= inp+10:
        num = x[pos1]+x[pos2]
        if num >= 10:
            x.append(num//10)
            x.append(num%10)
        else:
            x.append(num)
        pos1 = (pos1+x[pos1]+1)%len(x)
        pos2 = (pos2+x[pos2]+1)%len(x)
    print (''.join(map(str, x[inp:inp+10])))