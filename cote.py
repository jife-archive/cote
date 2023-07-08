import sys
input = sys.stdin.readline

Nlist = [list(input().split())for _ in range(7)]
cnt = 0

for i in range(7):
    for j in range(7):
        if j < 3:
            if Nlist[i][j] == Nlist[i][j+4]:
                print(i+1,"열","[",Nlist[i][j] , Nlist[i][j+1], Nlist[i][j+2], Nlist[i][j+3], Nlist[i][j+4],"]")
                cnt += 1
        elif i < 3 :
            if Nlist[j][i] == Nlist[j][i+4]:
                print(j+1,"행","[",Nlist[j][i] , Nlist[j][i+1], Nlist[j][i+2], Nlist[j][i+3], Nlist[j][i+4],"]")
                cnt += 1
 
print(cnt)