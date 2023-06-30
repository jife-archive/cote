import sys

N = int(sys.stdin.readline())
Nlist = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
Mlist = list(map(int, sys.stdin.readline().split()))

find = set(Nlist)
result = []

for num in Mlist:
    if num in find:
        result.append(1)
    else:
        result.append(0)

print(*result)
