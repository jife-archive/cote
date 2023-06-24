#수 들의 합
N, K = map(int,input().split())
x= []
if 1<= N <= 1000 and 1<= K <= N:
    x = list(map(int, input().split()))
    if len(x) != N:
        print("Error")
    else:
        x.sort()

print(x[-K])