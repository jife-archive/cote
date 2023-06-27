
import sys

N = int(sys.stdin.readline())
sum = 0
if N>=3 and N<=20 and N%2==1:
    Nlist = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    M = int(sys.stdin.readline())
    if M>=1 and M<=10:
        Mlist = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
        for i in range(M):
            row = Mlist[i][0]
            direction = Mlist[i][1]
            cnt = Mlist[i][2]
            for j in range(cnt):
                        if row <= N and direction == 0:
                            Nlist[row].append(Nlist[row].pop(0)) ##0번 인덱스의 자료를 팝하고 뒤에거 댕김
                        elif row <= N and direction == 1:
                             Nlist[row].insert(0,Nlist[row].pop())##inset는 0번자리에 값을 넣어라 -> pop()젤 뒤의 데이터를 갖고온다            
else:
    print("error")

q = 0
r = N-1
print(Nlist)
for i in range(N):
    print("i:",i)
    for j in range(q,r+1):
        print(Nlist[i][j])
        sum += Nlist[i][j]
    if i < N//2:
        q+=1
        r-=1
    else:
        q-=1
        r+=1    
print("총합:",sum)