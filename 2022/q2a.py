import sys
score = 0
for line in sys.stdin:
    s, t = line.strip().split()
    m = {
        ('A', 'X'): 4,
        ('A', 'Y'): 8,
        ('A', 'Z'): 3,
        ('B', 'X'): 1,
        ('B', 'Y'): 5,
        ('B', 'Z'): 9,
        ('C', 'X'): 7,
        ('C', 'Y'): 2,
        ('C', 'Z'): 6,
    }
    score += m[(s, t)]
print(score)