import sys

items = [line.strip() for line in sys.stdin]
items.sort()

cur_guard = None
guards = {}
for item in items:
    rel = item.split(':')
    minstr, logstr = rel[1].split('] ')
    minint = int(minstr)
    if logstr[0] == 'G':
        cur_guard = int(logstr.split()[1][1:])
    else:
        if cur_guard not in guards:
            guards[cur_guard] = []
        guards[cur_guard].append((minint, -1 if logstr[0] == 'w' else 1))
bestguard = None
bestsleeptime = 0
bestminute = None
for guard in guards:
    events = guards[guard]
    events.sort()
    maxsleepdays = 0
    nowtime = -100
    sleepdays = 0
    sleeptime = 0
    lastsleepdays = 0
    minutewithmaxsleepdays = None
    maxsleepdays = 0
    i = 0
    for i in range(len(events)):
        time, delta = events[i]
        sleepdays += delta
        if i >= len(events)-1 or events[i+1][0] != time:
            sleeptime += lastsleepdays*(time-nowtime)
            lastsleepdays = sleepdays
            nowtime = time
            if sleepdays > maxsleepdays:
                maxsleepdays = sleepdays
                minutewithmaxsleepdays = time
    if sleeptime > bestsleeptime:
        bestguard = guard
        bestsleeptime = sleeptime
        bestminute = minutewithmaxsleepdays
print(bestguard*bestminute)
