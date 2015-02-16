

import ch06_8queen_hettingers as het
import ch06_8queen_howell as how
import ch06_8queen_basic as ba
import ch06_8queen_hettingers_gf as het_gf

n = 8

het_answers = het.queen(n)
print(len(het_answers))
print(het_answers)

how_answers = how.queen(n)
# for answer in answers:
    # print(list(enumerate(answer, start=1)))
    #print(answer)

print(len(how_answers))
print(how_answers)

ba_answers = ba.queen(n)
print(len(ba_answers))
print(ba_answers)

queen_het_g = het_gf.queen_gf(n)
het_g_answers = [x for x in queen_het_g]

#if set(iter(het_answers)) == set(iter(how_answers)):
if set(het_answers) == set(how_answers) == set(ba_answers) == set(het_g_answers):
    print('yes')
else:
    print('no')

