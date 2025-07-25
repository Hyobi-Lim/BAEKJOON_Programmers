from collections import deque
def solution(board):
    answer = -1
    start_x,start_y=0,0
    end_x,end_y=0,0
    for i in range(len(board)):
        board[i]=list(board[i])
        for j in range(len(board[i])):
            if board[i][j]=='R':
                start_x,start_y=i,j
            elif board[i][j]=='G':
                end_x,end_y=i,j
    queue=deque()
    visited=set()
    queue.append((start_x,start_y,0))
    while queue:
        now_x,now_y,cnt=queue.popleft()
        if (now_x==end_x and now_y==end_y):
            answer=cnt
            break
        if ((now_x,now_y) in visited):
            continue
        visited.add((now_x,now_y))
        count=0
        if 0<=now_x-1 and board[now_x-1][now_y]!='D':
            count+=1
            while(0<=now_x-count and board[now_x-count][now_y]!='D'):
                count+=1
            count-=1
            queue.append((now_x-count,now_y,cnt+1))
        count=0
        if 0<=now_y-1 and board[now_x][now_y-1]!='D':
            count+=1
            while(0<=now_y-count and board[now_x][now_y-count]!='D'):
                count+=1
            count-=1
            queue.append((now_x,now_y-count,cnt+1))
        
        count=0
        if now_x+1<len(board) and board[now_x+1][now_y]!='D':
            count+=1
            while(now_x+count<len(board) and board[now_x+count][now_y]!='D'):
                count+=1
            count-=1
            queue.append((now_x+count,now_y,cnt+1))
        count=0
        if now_y+1<len(board[0]) and board[now_x][now_y+1]!='D':
            count+=1
            while(now_y+count<len(board[0]) and board[now_x][now_y+count]!='D'):
                count+=1
            count-=1
            queue.append((now_x,now_y+count,cnt+1))
    return answer