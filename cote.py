#숫자만 추출

s = input()
res = 0
cnt = 0
for i in s:
    if i.isdecimal() == True:
        res = res * 10 + int(i)
print(res)

for j in range(1, res+1):
    if res % j == 0:
        cnt += 1
print(cnt)
        