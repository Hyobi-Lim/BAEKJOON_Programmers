import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
for i in list(combinations(arr,m)):
    print(*i)