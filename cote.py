import sys

N = int(sys.stdin.readline())
Nlist = [[]for _ in range(N)]

for i in range(N):
    age,name=  map(str,sys.stdin.readline().split()) 
    Nlist[i] += int(age),name

Nlist.sort(key=lambda x: x[0])

for i in Nlist:
    print(i[0],i[1])