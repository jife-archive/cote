import sys



def check(checklist):
    for i in range(9):
        Rowchecklist = [0] * 10
        Colchecklist = [0] * 10
        for j in range(9):
            Rowchecklist[checklist[i][j]] = 1
            Colchecklist[checklist[j][i]] = 1
        if sum(Rowchecklist) or sum(Colchecklist) != 9:
            return False
    for i in range(3):
        for j in range(3):
            groupchecklist = [0] * 10
            for k in range(3):
                for v in range(3):
                    groupchecklist[checklist[i*3 + k][j*3 +v]] = 1
            if sum(groupchecklist) != 9:
                return False
    return True
Nlist = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]

if check(Nlist):
    print("YES")
else:
    print("NO")
