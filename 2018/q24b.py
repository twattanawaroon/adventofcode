import sys

def parse(side, idx, s):
    t0, t1 = s.split('with an attack that does')
    t2, t3 = t1.split('damage at initiative')
    initiative = int(t3.strip())
    t4, t5 = t2.strip().split()
    dmg_val = int(t4.strip())
    dmg_type = t5.strip()
    t6, t7 = t0.strip().split('hit points')
    immunes = set()
    weaks = set()
    stripper = lambda t: t.strip()
    if len(t7.strip()) > 0:
        tpcs = map(stripper, t7.strip()[1:-1].split(';'))
        for tpc in tpcs:
            t8, t9 = map(stripper, tpc.split('to'))
            objs = set(map(stripper, t9.split(',')))
            if t8 == 'immune':
                immunes = objs
            elif t8 == 'weak':
                weaks = objs
            else:
                print('wtf')
    u0, u1 = t6.split('units each with')
    unit_count = int(u0.strip())
    unit_hp = int(u1.strip())
    return [idx, side, unit_count, unit_hp, immunes, weaks, dmg_val, dmg_type, initiative]

def one_sided(x):
    return len(x) == 0 or all(map(lambda s: s[1] == x[0][1], x))

def get_damage(team1, team2):
    idx1, side1, unit_count1, unit_hp1, immunes1, weaks1, dmg_val1, dmg_type1, initiative1 = team1
    idx2, side2, unit_count2, unit_hp2, immunes2, weaks2, dmg_val2, dmg_type2, initiative2 = team2
    base_dmg = unit_count1*dmg_val1
    if dmg_type1 in immunes2:
        return 0
    elif dmg_type1 in weaks2:
        return base_dmg*2
    else:
        return base_dmg

side = 0
idx = 0
y = []
for line in sys.stdin:
    s = line.strip()
    if s.endswith(':'):
        side += 1
    elif len(s) > 0:
        y.append(parse(side, idx, s))
        idx += 1

def determine_winner(y, boost):
    x = []
    for team0 in y:
        team1 = team0[:]
        if team1[1] == 1:
            team1[6] += boost
        x.append(team1)
    kills = 1
    while not one_sided(x) and kills > 0:
        x.sort(key=lambda s: (-s[2]*s[6], -s[8]))
        target = dict()
        targeted = set()
        for team1 in x:
            best_dmg = (0, 0, 0)
            best_team2 = None
            for team2 in x:
                idx1, side1, unit_count1, unit_hp1, immunes1, weaks1, dmg_val1, dmg_type1, initiative1 = team1
                idx2, side2, unit_count2, unit_hp2, immunes2, weaks2, dmg_val2, dmg_type2, initiative2 = team2
                if idx2 not in targeted and side1 != side2:
                    dmg = get_damage(team1, team2)
                    dmg_compound = (dmg, unit_count2*dmg_val2, initiative2)
                    if dmg > 0 and dmg_compound > best_dmg:
                        best_dmg = dmg_compound
                        best_team2 = team2
            if best_team2 is not None:
                target[idx1] = best_team2
                targeted.add(best_team2[0])
        kills = 0
        x.sort(key=lambda s: -s[8])
        for team1 in x:
            idx1, side1, unit_count1, unit_hp1, immunes1, weaks1, dmg_val1, dmg_type1, initiative1 = team1
            if unit_count1 <= 0 or idx1 not in target:
                continue
            team2 = target[idx1]
            idx2, side2, unit_count2, unit_hp2, immunes2, weaks2, dmg_val2, dmg_type2, initiative2 = team2
            dmg = get_damage(team1, team2)
            kill = min(team2[2], dmg//team2[3])
            team2[2] -= kill
            kills += kill
        x = list(filter(lambda s: s[2] > 0, x))
    if not one_sided(x):
        return None, None
    return x[0][1], sum(map(lambda s: s[2], x))

boost = 0
winner = None
while winner is None or winner == 2:
    winner, ans = determine_winner(y, boost)
    boost += 1
print(ans)