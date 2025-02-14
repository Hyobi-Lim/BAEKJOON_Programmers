import sys
n,m=map(int,sys.stdin.readline().split())
poketmon=dict()
poketmonnum=dict()
for i in range(1,n+1):
    nowpoketmon=sys.stdin.readline().strip()
    poketmon[nowpoketmon]=i
    poketmonnum[str(i)]=nowpoketmon
for i in range(m):
    now=sys.stdin.readline().strip()
    if now in poketmon:
        print(poketmon[now])
    else:
        print(poketmonnum[now])