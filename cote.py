
import sys
input = sys.stdin.readline
N = int(input())

Nlist = [0 for _ in range(N)]
rowsum = []
colsum = []
carsum = [0,0]
if 1<=N and N<=50:
    for i in range(N):
        Nlist[i] = list(map(int,input().split()))

    rowsum = [sum(row)for row in Nlist]
    colsum = [sum(col)for col in zip(*Nlist)]
    for i in range(N):
        carsum[0] += Nlist[i][i]
        carsum[1] += Nlist[i][-1-i]
    rowsum.sort()
    colsum.sort()
    carsum.sort()
    totalsum = []
    totalsum.append(rowsum[-1])
    totalsum.append(colsum[-1])
    totalsum.append(carsum[-1])
    print(max(totalsum))
else:
    print("error")
