n = int(input("n:"))
s=[]

for i in range(n):
    s.append(input("s:"))
    s[i].upper()
    for j in range(len(s[i])//2):
        if s[i][j] == s[i][-1-j]:
            print(s[j],s[-1-j])
            break
        else:
            print(s[i]+"회문x")
            break

#회문 문자열 검사
    