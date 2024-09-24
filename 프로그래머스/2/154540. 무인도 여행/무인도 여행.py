import sys
sys.setrecursionlimit(10**6)
dr = [-1,0,1,0]
dc = [0,1,0,-1]
cnt = 0
def DFS(r, c, a, b, arr):
    global cnt
    cnt += int(arr[r][c])
    arr[r] = arr[r][:c]+'X'+arr[r][c+1:]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if nr<0 or nr>= a or nc <0 or nc>=b:
            continue
        if arr[nr][nc] == 'X':
            continue
        DFS(nr, nc, a, b, arr)
def solution(maps):
    global cnt
    answer = []
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X':
                cnt = 0 
                DFS(i, j, len(maps), len(maps[i]), maps)
                answer.append(cnt)
    if len(answer)==0:
        answer=[-1]
    else:
        answer.sort()
    print(maps)
    return answer