import sys
from itertools import permutations
n,m=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
arr.sort()
for i in list(permutations(arr,m)):
    print(*i)