import sys
from itertools import combinations
n,s=map(int,sys.stdin.readline().split())
arr=list(map(int,sys.stdin.readline().split()))
answer=0
for i in range(1,n+1):
    for j in combinations(arr,i):
        if sum(j)==s:
            answer+=1
print(answer)