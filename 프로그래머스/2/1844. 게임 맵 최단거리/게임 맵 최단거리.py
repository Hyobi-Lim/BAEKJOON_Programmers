dr=[0,1,0,-1]
dc=[1,0,-1,0]
def BFS(r, c,N,M,dist,arr):
    Q = []
    Q.append((r, c))
    dist[r][c] = 1
    while Q:
        curr_r, curr_c = Q.pop(0)
        for i in range(4):
            nr = curr_r + dr[i]
            nc = curr_c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue
            if arr[nr][nc] == 0 or dist[nr][nc] != 0:
                continue

            Q.append((nr, nc))
            dist[nr][nc] = dist[curr_r][curr_c] + 1
def solution(maps):
    N=len(maps)
    M=len(maps[0])
    dist = [[0]*M for _ in range(N)]
    BFS(0,0,N,M,dist,maps)
    if dist[N-1][M-1]==0:
        answer=-1
    else:
        answer=dist[N-1][M-1] 
    return answer