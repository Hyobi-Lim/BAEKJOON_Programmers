import sys
from itertools import product
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
all=list(set(product(arr,repeat=m)))
all.sort()
for i in all:
    print(*i)