import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
not_tgt=set()
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    for j in range(1,n+1):
        if j!=a and j!=b:
            now=[a,b,j]
            now.sort()
            not_tgt.add(tuple(now))
all_combination=list(combinations([j for j in range(1,n+1)],3))
print(len(all_combination)-len(not_tgt))