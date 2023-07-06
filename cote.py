import sys

input = sys.stdin.readline

N = int(input())
Nlist = list(input().split())
M= int(input())
Mlist = list(input().split())

cnt = {}

for i in Nlist:
    if i in cnt:
        cnt[i] +=1
    else:
        cnt[i] = 1
for i in Mlist:
    if i in cnt:
        print(cnt[i],end=" ")
    else:
        print(0,end=" ")

print("")