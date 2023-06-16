#카드 역배치

List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
k = list(map(int, input().split()))
if k[1] < k [0]:
    tmp = k[0]
    k[0] = k[1]
    k[1] = tmp

n= k[1] - k[0]

for i in range(n//2):
    List[(k[0]-1)+i],List[(k[1]-1)-i] =List[(k[1]-1)-i],List[(k[0]-1)+i]

print(List)



   