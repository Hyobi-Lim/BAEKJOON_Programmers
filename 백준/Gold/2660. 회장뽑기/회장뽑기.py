import sys
from collections import deque
n=int(sys.stdin.readline())
friends=[[] for _ in range(n+1)]
while(1):
    a,b=map(int,sys.stdin.readline().split())
    if a==-1 and b==-1:
        break
    else:
        friends[a].append(b)
        friends[b].append(a)
def bfs(graph,start,distance):
    adjacency_nodes=deque([start])
    visited=set([start])
    while adjacency_nodes:
        now=adjacency_nodes.popleft()
        visited.add(now)
        for i in friends[now]:
            if i not in visited and i not in adjacency_nodes:
                adjacency_nodes.append(i)
                distance[i]=distance[now]+1
    return distance
max_distance=[0]*(n+1)
for i in range(1,n+1):
    distance=[0]*(n+1)
    bfs(friends,i,distance)
    max_distance[i]=max(distance)
max_distance_dict=dict()
for i in range(1,n+1):
    if max_distance[i] in max_distance_dict:
        max_distance_dict[max_distance[i]].append(i)
    else:
        max_distance_dict[max_distance[i]]=[i]
print(min(max_distance_dict),len(max_distance_dict[min(max_distance_dict)]))
for i in max_distance_dict[min(max_distance_dict)]:
    print(i,end=' ')