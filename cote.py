
import sys

Nlist = []
N = int(sys.stdin.readline())

while (N>0):
    Nlist = Nlist + [N%10]
    N //= 10

Nlist.sort(reverse=True)
Nlist = list(map(str, Nlist))
a = "".join(Nlist)
print(a)



