import sys
from itertools import combinations_with_replacement
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
all=list(set(combinations_with_replacement(arr,m)))
all.sort()
for i in all:
    print(*i)