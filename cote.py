import sys
input = sys.stdin.readline

n, m  = map(int,input().split())
arr1 = []
arr2 = []

for i in range(n):
    x = input()
    arr1.append(x)
for j   in range(m):
    x = input()
    arr2.append(x)
result = list(set(arr1)&set(arr2))
result.sort()

print(len(result))
print(''.join(result),end="")