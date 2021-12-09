import sys

zz = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
count = 0
for line in sys.stdin:
    x = line.strip().split('|')
    a = x[0].strip().split()
    b = x[1].strip().split()
    freq = dict()
    m = dict()
    for item in a:
        for c in item:
            if c not in freq:
                freq[c] = 0
            freq[c] += 1
        if len(item) == 4:
            four = item
    for item in freq:
        if freq[item] == 8 and item not in four:
            m[item] = 'a'
        elif freq[item] == 6:
            m[item] = 'b'
        elif freq[item] == 8 and item in four:
            m[item] = 'c'
        elif freq[item] == 7 and item in four:
            m[item] = 'd'
        elif freq[item] == 4:
            m[item] = 'e'
        elif freq[item] == 9:
            m[item] = 'f'
        elif freq[item] == 7 and item not in four:
            m[item] = 'g'
    num = 0
    for item in b:
        y = [m[c] for c in item]
        y.sort()
        s = ''.join(y)
        num *= 10
        num += zz.index(s)
    count += num

print(count)
