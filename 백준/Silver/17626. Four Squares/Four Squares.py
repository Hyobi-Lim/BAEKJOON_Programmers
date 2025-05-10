import sys,math
from itertools import product
n=int(sys.stdin.readline())
answer=0
if math.isqrt(n)**2==n:
    answer=1
    print(answer)
if answer==0:
    for i in range(math.isqrt(n-1),0,-1):
        for j in range(i,0,-1):
            if i**2+j**2<n:
                break
            elif i**2+j**2==n:
                answer=2
                print(answer)
                break
        if answer!=0:
            break
if answer==0:
    for i in range(math.isqrt(n-2),0,-1):
        for j in range(i,0,-1):
            for k in range(j,0,-1):
                if i**2+j**2+k**2<n:
                    break
                elif i**2+j**2+k**2==n:
                    answer=3
                    print(answer)
                    break
            if answer!=0:
                break
        if answer!=0:
            break
if answer==0:
    print(4)