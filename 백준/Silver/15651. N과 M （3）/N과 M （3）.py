import sys
from itertools import product
n,m=map(int,sys.stdin.readline().split())
arr=[str(i) for i in range(1,n+1)]
for i in product(arr,repeat=m):
    print(*i)