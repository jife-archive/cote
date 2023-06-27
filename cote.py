
import sys

N = int(sys.stdin.readline())
result = []

Nlist = [sys.stdin.readline().strip() for _ in range(N)] 


result = list(set(Nlist))
result.sort()
result.sort(key=lambda x: len(x))

for i in range(len(result)):
    print(result[i])