import sys
sys.setrecursionlimit(10**6)
n=int(sys.stdin.readline())
edge=[[] for _ in range(n+1)]
visited=set()
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)
all_edge=0
def find_way(edge,now,count):
    global all_edge
    num=0
    visited.add(now)
    for i in edge[now]:
        if i not in visited:
            find_way(edge,i,count+1)
            num+=1
    if num==0:
        all_edge+=count
find_way(edge,1,0)
if all_edge%2==0:
    print("No")
else:
    print("Yes")