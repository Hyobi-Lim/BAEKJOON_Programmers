import sys
node=int(sys.stdin.readline())
n=int(sys.stdin.readline())
all_node=[[0]*(node+1) for _ in range(node+1)]
for i in range(n):
    a,b=map(int,sys.stdin.readline().split())
    all_node[a][b]=1
    all_node[b][a]=1
stack=[1]
visited=[]
while(len(stack)>0):
    now=stack.pop()
    if now not in visited:
        visited.append(now)
        for i in range(node+1):
            if all_node[now][i]==1 and i not in visited:
                stack.append(i)
print(len(visited)-1)