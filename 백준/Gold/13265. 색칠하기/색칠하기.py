import sys		
t=int(sys.stdin.readline())
for i in range(t):
    n,m=map(int,sys.stdin.readline().split())
    answer='possible'
    edges=[[] for _ in range(n+1)]
    edgecolor=[-1]*(n+1)
    edgecolor[0]=1
    edgecolor[1]=1
    for j in range(m):
        x,y=map(int,sys.stdin.readline().split())
        edges[x].append(y)
        edges[y].append(x)
    stack=[1]
    visited=set()
    while(stack):
        if answer=='impossible':
            break
        now=stack.pop()
        if now not in visited:
            visited.add(now)
            num=edgecolor[now]+1
            for j in edges[now]:
                if j not in visited:
                    stack.append(j)
                if edgecolor[j]==-1:
                    edgecolor[j]=num%2
                elif edgecolor[j]==num%2:
                    continue
                else:
                    answer='impossible'
                    break
        if len(stack)==0 and len(visited)!=n:
            for j in range(1,n+1):
                if j not in visited:
                    stack.append(j)
                    break
    print(answer)       