
import sys
N = int(sys.stdin.readline())
Nlist = [0] * 10001

if 1<=N and N<=10000000:
    for i in range(N):
     num = int(sys.stdin.readline())
     Nlist[num] += 1
     if Nlist[i] > N:
        print("error")
        continue
 
    for i in range(10001):
       if Nlist[i] != 0:
          for j in range(Nlist[i]):
             print(i)          
else:
    print("Error")

