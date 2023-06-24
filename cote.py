#수 들의 합

import random
nlist = []
sum = 0
avg = 0
for i in range(5):
   nlist.append(int(input()))

for i in range(5):
   sum  += nlist[i]
   if i == 4:
      avg = sum //5
nlist.sort()
print(avg)
print(nlist[2])
    
