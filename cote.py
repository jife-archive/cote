#두 리스트 합치기
import random

a = int(input())
b =int(input())

alist = random.sample(range(1,100),a)
blist = random.sample(range(1,100),b)
alist.sort()
blist.sort()

#sumlist = alist + blist
#sumlist.sort()  시간복잡도 때문에 다른거 사용

p1 = 0
p2 = 0 
sumlist = []

while p1< len(alist) and p2<len(blist):
    if alist[p1] <= blist[p2]:
        sumlist.append(alist[p1])
        p1 += 1
    else:
        sumlist.append(blist[p2])
        p2 += 1
if p1< a:
    sumlist = sumlist + alist[p1:]
if p2 <b:
    sumlist = sumlist + blist[p2:]

print(sumlist)


   