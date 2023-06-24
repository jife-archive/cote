#수 들의 합
import random

n = int(input())
c = int(input())
nlist = []

for i in range(n):
    nlist.append(random.randint(1,c))

lt = 0
rt = 1
cnt = 0
tot = nlist[0]
while 1:
    if tot < c:
        if rt < n:
            tot += nlist[rt]
            rt += 1
        else:
            break
    elif tot == c:
        cnt += 1
        tot -= nlist[lt]
        lt += 1
    else:
        tot -= nlist[lt]
        lt += 1


print(nlist)
print(cnt)