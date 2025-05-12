import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
all=list(set(combinations(arr,m)))
all.sort()
for i in all:
    print(*i)