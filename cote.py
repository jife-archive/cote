import sys

N = int(sys.stdin.readline())
Nlist = [[]for _ in range(N)]
topcount = 0
if N < 1 and N >50:
    print("error")
else:
    for i in range(N):
        Nlist[i] += list(map(int,(sys.stdin.readline().split())))

x=[-1,0,1,0]
y=[0,1,0,-1]
Nlist.insert(0,[0]*N)
Nlist.append([0]*N)

for i in Nlist:
    i.insert(0,0)
    i.append(0)

for i in range(1,N+1):
    for j in range(1,N+1):
        if all(Nlist[i][j]>Nlist[i+x[k]][j+y[k]]for k in range(4)):
            topcount += 1
            print(i,"번째",j,"칸",Nlist[i][j])
print(topcount)