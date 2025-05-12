import sys
from itertools import combinations_with_replacement
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
for i in list(combinations_with_replacement(arr,m)):
    print(*i)