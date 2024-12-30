from collections import deque
def solution(n, edge):
    answer = 0
    matrix=dict()
    for i in range(1,n+1):
        matrix[i]=[]
    for i in range(len(edge)):
        matrix[edge[i][0]].append(edge[i][1])
        matrix[edge[i][1]].append(edge[i][0])
    queue=deque([1])
    visited=set()
    while queue:
        newqueue=deque()
        for now in queue:
            if now not in visited:
                visited.add(now)
            for i in matrix[now]:
                if i not in visited:
                    visited.add(i)
                    newqueue.append(i)
                    matrix[i].remove(now)
            if newqueue:
                answer=len(newqueue)
            queue=newqueue
    return answer