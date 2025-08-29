import math,heapq
def solution(N, road, K):
    answer = 0
    distance=[math.inf]*(N+1)
    distance[1]=0
    roadmap=[[] for _ in range(N+1)]
    for a,b,c in road:
        roadmap[a].append([b,c])
        roadmap[b].append([a,c])
    heap=[(1,0)]
    while heap:
        now,d=heapq.heappop(heap)
        if distance[now]<d:
            continue
        for next_node,weight in roadmap[now]:
            next_distance=d+weight
            if(distance[next_node]>next_distance):
                distance[next_node]=next_distance
                heapq.heappush(heap,(next_node,next_distance))
    for i in distance:
        if i<=K:
            answer+=1
    return answer