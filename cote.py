n,k = map(int,input().split())
nList = []
for i in range(1,n):
    if n % i == 0 :
        nList.append(i)

if len(nList) < k :
    print("-1")
else:
    print(nList[k-1])
