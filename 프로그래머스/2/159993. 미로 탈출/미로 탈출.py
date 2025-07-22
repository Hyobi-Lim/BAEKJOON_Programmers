from collections import deque
def solution(maps):
    answer = -1
    start=[]
    for i in range(len(maps)):
        maps[i]=list(maps[i])
        for j in range(len(maps[i])):
            if maps[i][j]=='S':
                start=[i,j]
    lever=deque()
    lever.append((start[0],start[1],0))
    lever_cnt=0
    dx=[-1,0,1,0]
    dy=[0,1,0,-1]
    visited=set()
    while lever:
        now_x,now_y,now_cnt=lever.popleft()
        if (now_x,now_y) in visited:
            continue
        visited.add((now_x,now_y))
        if maps[now_x][now_y]=='L':
            start=[now_x,now_y]
            lever_cnt=now_cnt
            break
        else:
            for i in range(4):
                if (now_x+dx[i],now_y+dy[i]) not in visited and 0<=now_x+dx[i]<len(maps) and 0<=now_y+dy[i]<len(maps[0]) and maps[now_x+dx[i]][now_y+dy[i]] in ['O','E','L']:
                    lever.append((now_x+dx[i],now_y+dy[i],now_cnt+1))
    if lever_cnt==0:
        return -1
    else:
        exit=deque()
        exit.append((start[0],start[1],0))
        exit_cnt=0
        visited=set()
        while exit:
            now_x,now_y,now_cnt=exit.popleft()
            if (now_x,now_y) in visited:
                continue
            visited.add((now_x,now_y))
            if maps[now_x][now_y]=='E':
                exit_cnt=now_cnt
                break
            else:
                for i in range(4):
                    if (now_x+dx[i],now_y+dy[i]) not in visited and 0<=now_x+dx[i]<len(maps) and 0<=now_y+dy[i]<len(maps[0]) and maps[now_x+dx[i]][now_y+dy[i]] in ['O','E','S']:
                        exit.append((now_x+dx[i],now_y+dy[i],now_cnt+1))
        if exit_cnt==0:
            return -1
        else:
            return lever_cnt+exit_cnt