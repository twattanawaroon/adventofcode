import sys
count2 = 0
count3 = 0

def process(text):
    h2 = False
    h3 = False
    lcount = {}
    for c in text:
        if c not in lcount:
            lcount[c] = 0
        lcount[c] += 1
    for c in lcount:
        if lcount[c] == 2:
            h2 = True
        if lcount[c] == 3:
            h3 = True
    return h2, h3

for line in sys.stdin:
    has2, has3 = process(line.strip())
    count2 += has2
    count3 += has3
print(count2*count3)