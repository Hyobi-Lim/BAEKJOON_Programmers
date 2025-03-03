import sys
import math
import heapq
n,m=map(int,sys.stdin.readline().split())
graph=dict()
for i in range(m):
    a,b,c=map(int,sys.stdin.readline().split())
    if a not in graph:
        graph[a]=[(b,c)]
    else:
        graph[a].append((b,c))
    if b not in graph:
        graph[b]=[(a,c)]
    else:
        graph[b].append((a,c))
def dijkstra(graph,node):
    node_from={node:None for node in graph}
    lead_time={node:math.inf for node in graph}
    lead_time[node]=0
    visited=set()
    heap=[]
    heapq.heappush(heap,(0,node))
    while heap:
        prev_time,prev_node=heapq.heappop(heap)
        if prev_node not in visited:
            visited.add(prev_node)
        for v,weight in graph[prev_node]:
            if prev_time+weight<lead_time[v]:
                lead_time[v]=prev_time+weight
                node_from[v]=prev_node
                heapq.heappush(heap,(lead_time[v],v))
    return lead_time,node_from
node_from,lead_time=dijkstra(graph,1)
print(node_from[n])