import sys

N = int(sys.stdin.readline())
Nlist = [[]for _ in range(N)]
topcount = 0
if N < 1 and N >50:
    print("error")
else:
    for i in range(N):
        Nlist[i] += list((sys.stdin.readline().split()))

t = b = l = r = 0

for i in range(N):
    if i == 0 or i == N-1:
        if i == 0:
            t = 0
            b = i+1
        elif i == N-1:
            t = i-1
            b = 0
    else:
        t = i -1
        b = i+1
    for j in range(N):
        if j == N-1:
            l = j-1
            if t == 0:
                if Nlist[i][j] > Nlist[i][l] and Nlist[i][j] > Nlist[b][j]:
                    topcount +=1
                    print(i+1,"번째",Nlist[i][j],j+1,"칸")
            elif b == 0:
                if Nlist[i][j] > Nlist[t][j] and Nlist[i][j] > Nlist[i][l]:
                    topcount += 1
                    print(i+1,"번째",Nlist[i][j],j+1,"칸")
            elif t > 0 and b > 0:
                if Nlist[i][j] > Nlist[i][l] and Nlist[i][j] > Nlist[b][j] and Nlist[i][j] > Nlist[t][j]:
                    topcount +=1
                    print(i+1,"번째",Nlist[i][j],j+1,"칸")
        if j == 0:
            r = j+1
            if t == 0:
                if Nlist[i][j] > Nlist[i][r] and Nlist[i][j] > Nlist[b][j]:
                    topcount +=1
                    print(i+1,"번째",Nlist[i][j],j+1,"칸")
            elif b == 0:
                if Nlist[i][j] > Nlist[i][r] and Nlist[i][j] > Nlist[t][j]:
                    topcount +=1
                    print(i+1,"번째",Nlist[i][j],j+1,"칸")
            elif t > 0 and b >0:
                if Nlist[i][j] > Nlist[i][l] and Nlist[i][j] > Nlist[b][j] and Nlist[i][j] > Nlist[t][j]and Nlist[i][j]>Nlist[i][r]:
                    print(i+1,"번째",Nlist[i][j],j+1,"칸")
                    topcount +=1
                
        if j > 0 and j < N -1:
            r = j+1
            l = j-1
            if t == 0:
                if Nlist[i][j] > Nlist[i][r] and Nlist[i][j] > Nlist[b][j] and Nlist[i][j] > Nlist[i][l]:
                    topcount +=1
                    print(i+1,"번째",Nlist[i][j],j+1,"칸")
            if b == 0:
                if Nlist[i][j] > Nlist[i][r] and Nlist[i][j] > Nlist[t][j] and Nlist[i][j] > Nlist[i][l]:
                    topcount +=1
                    print(i+1,"번째",Nlist[i][j],j+1,"칸")
            if t > 0 and b > 0:
                if Nlist[i][j] > Nlist[i][l] and Nlist[i][j] > Nlist[b][j] and Nlist[i][j] > Nlist[t][j]and Nlist[i][j]>Nlist[i][r]:
                    print(i+1,"번째",Nlist[i][j],j+1,"칸")
                    topcount +=1
                
print(topcount)
