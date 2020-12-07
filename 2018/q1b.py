import sys
count = 0
freqlist = [int(line) for line in sys.stdin]
found = set()
i = 0
while count not in found:
    found.add(count)
    count += freqlist[i%len(freqlist)]
    i += 1
print(count)