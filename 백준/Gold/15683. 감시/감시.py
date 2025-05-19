import sys
from copy import deepcopy
n,m=map(int,sys.stdin.readline().split())
arr=[list(map(int, input().split())) for _ in range(n)]
cctv=[]
for i in range(n):
    for j in range(m):
        if arr[i][j] in [1,2,3,4,5]:
            cctv.append([i,j])
answer=n*m
def blind_spot(arr,cctv):
    global answer
    if len(cctv)==0:
        cnt_cctv=0
        for i in range(n):
            for j in range(m):
                if arr[i][j]==0:
                    cnt_cctv+=1
        if answer>cnt_cctv:
            answer=cnt_cctv
        return
    now=cctv.pop()
    if arr[now[0]][now[1]]==1:
        now_arr=deepcopy(arr)
        for k in range(now[1],-1,-1):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[0],-1,-1):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[1]+1,m):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[0]+1,n):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        blind_spot(now_arr,cctv)
        cctv.append(now)
    elif arr[now[0]][now[1]]==2:
        now_arr=deepcopy(arr)
        for k in range(now[1],-1,-1):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        for k in range(now[1]+1,m):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[0],-1,-1):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        for k in range(now[0]+1,n):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        blind_spot(now_arr,cctv)
        cctv.append(now)
    elif arr[now[0]][now[1]]==3:
        now_arr=deepcopy(arr)
        for k in range(now[1],-1,-1):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        for k in range(now[0],-1,-1):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[0],-1,-1):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        for k in range(now[1]+1,m):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[1]+1,m):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        for k in range(now[0]+1,n):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[0]+1,n):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        for k in range(now[1],-1,-1):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        blind_spot(now_arr,cctv)
        cctv.append(now)
    elif arr[now[0]][now[1]]==4:
        now_arr=deepcopy(arr)
        for k in range(now[1],-1,-1):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        for k in range(now[0],-1,-1):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        for k in range(now[1]+1,m):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[0],-1,-1):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        for k in range(now[1]+1,m):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        for k in range(now[0]+1,n):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[1]+1,m):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        for k in range(now[0]+1,n):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        for k in range(now[1],-1,-1):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        blind_spot(now_arr,cctv)
        now_arr=deepcopy(arr)
        for k in range(now[0]+1,n):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        for k in range(now[1],-1,-1):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        for k in range(now[0],-1,-1):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        blind_spot(now_arr,cctv)
        cctv.append(now)
    else:
        now_arr=deepcopy(arr)
        for k in range(now[1],-1,-1):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        for k in range(now[0],-1,-1):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        for k in range(now[1]+1,m):
            if now_arr[now[0]][k]==0:
                now_arr[now[0]][k]='#'
            elif now_arr[now[0]][k]==6:
                break
        for k in range(now[0]+1,n):
            if now_arr[k][now[1]]==0:
                now_arr[k][now[1]]='#'
            elif now_arr[k][now[1]]==6:
                break
        blind_spot(now_arr,cctv)
        cctv.append(now)
blind_spot(arr,cctv)
print(answer)