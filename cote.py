
import sys
import random

N = int(sys.stdin.readline())
sum = 0
if N<= 20 and N>=3 and N%2==1:
    Nlist = [[] for _ in range(N)]
    for i in range(N):
            Nlist[i] = list(map(int, sys.stdin.readline().split())) ##중요 한줄로 입력받기!
    s=e=N//2
    for i in range(N):
         print(i)    
         for j in range(s, e+1):
            sum += Nlist[i][j]   
         if i < N//2:
            s -=1
            e +=1
         else:
              s+=1
              e-=1          
else:
    print("Error")
print(sum)



