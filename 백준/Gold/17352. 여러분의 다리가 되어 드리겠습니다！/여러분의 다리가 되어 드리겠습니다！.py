import sys
n=int(sys.stdin.readline())
edge=[[] for _ in range(n+1)]
for i in range(n-2):
    a,b=map(int,sys.stdin.readline().split())
    edge[a].append(b)
    edge[b].append(a)
stack=[1]
visited=set()
while(stack):
    now=stack.pop()
    if now not in visited:
        visited.add(now)
        for i in edge[now]:
            if i  not in visited:
                stack.append(i)
for i in range(2,n+1):
    if i not in visited:
        print('1 '+str(i))
        break