import sys
import codelib as cl

ans = [0, 0]
fq = [0, 0, 0, 1, 3, 6, 7, 6, 3, 1]
m = dict()
m [(0, 0, 0, 7, 9)] = 1
for i in range(21):
    for j in range(21):
        for turn in range(2):
            for si in range(1, 11):
                for sj in range(1, 11):
                    if (i,j,turn,si,sj) in m:
                        w = m[(i,j,turn,si,sj)]
                        if turn == 0:
                            for dies in range(3, 10):
                                v = w*fq[dies]
                                nsi = cl.mod_start1(si+dies, 10)
                                ni = i+nsi
                                if ni >= 21:
                                    ans[turn] += v
                                else:
                                    cl.dict_add(m, (ni,j,1-turn,nsi,sj), v)
                        else:
                            for dies in range(3, 10):
                                v = w*fq[dies]
                                nsj = cl.mod_start1(sj+dies, 10)
                                nj = j+nsj
                                if nj >= 21:
                                    ans[turn] += v
                                else:
                                    cl.dict_add(m, (i,nj,1-turn,si,nsj), v)
print(max(ans))
