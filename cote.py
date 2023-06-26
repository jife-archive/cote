
import sys

N = int(sys.stdin.readline())
Nlist = [[]for _ in range(N)]

for  i in range(N):
    Nlist[i] = list(map(int, sys.stdin.readline().split()))

Nlist.sort()

for i in Nlist:
    print(i[0],i[1])
