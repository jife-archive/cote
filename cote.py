
import sys
input = sys.stdin.readline
N = int(input())

Nlist = []
if N < 1 and N >1000000:
    print("error")
else:
    for i in range(N):
        Nlist.append(int(input()))
    for i in sorted(Nlist):
        print(i)
                    
# sys.stdin.readline이 input()보다 빠르단것을 알게되었다. 흑흑 ㅠㅠ