import sys
from itertools import product
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
for i in list(product(arr,repeat=m)):
    print(*i)