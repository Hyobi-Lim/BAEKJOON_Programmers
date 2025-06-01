import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
fav_chicken=[list(map(int,input().split())) for _ in range(n)]
chicken=list(combinations([i for i in range(m)],3))
answer=0
for i in chicken:
    now=0
    for j in range(n):
        now+=max(fav_chicken[j][i[0]],fav_chicken[j][i[1]],fav_chicken[j][i[2]])
    if answer<now:
        answer=now
print(answer)