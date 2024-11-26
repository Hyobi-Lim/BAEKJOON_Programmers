def solution(places):
    answer = []
    def lrtb(arr,a,b,c):
        if 0<=c-1<=4 and arr[a][b][c-1]=='P':
            return 0
        elif 0<=c+1<=4 and arr[a][b][c+1]=='P':
            return 0
        elif 0<=b+1<=4 and arr[a][b+1][c]=='P':
            return 0
        elif 0<=b-1<=4 and arr[a][b-1][c]=='P':
            return 0
        else:
            return 1
    def lrtb2(arr,a,b,c):
        if 0<=c-2<=4 and arr[a][b][c-2]=='P' and arr[a][b][c-1]=='O':
                return 0
        elif 0<=c+2<=4 and arr[a][b][c+2]=='P' and arr[a][b][c+1]=='O':
                return 0
        elif 0<=b+2<=4 and arr[a][b+2][c]=='P' and arr[a][b+1][c]=='O':
                return 0
        elif 0<=b-2<=4 and arr[a][b-2][c]=='P' and arr[a][b-1][c]=='O':
                return 0
        else:
            return 1
    def diagonal(arr,a,b,c):
        if 0<=c-1<=4 and 0<=b-1<=4 and arr[a][b-1][c-1]=='P' and (arr[a][b][c-1]=='O' or arr[a][b-1][c]=='O'):
            return 0
        elif 0<=c+1<=4 and 0<=b-1<=4 and arr[a][b-1][c+1]=='P' and (arr[a][b][c+1]=='O' or arr[a][b-1][c]=='O'):
            return 0
        elif 0<=c-1<=4 and 0<=b+1<=4 and arr[a][b+1][c-1]=='P' and (arr[a][b][c-1]=='O' or arr[a][b+1][c]=='O'):
            return 0
        elif 0<=c+1<=4 and 0<=b+1<=4 and arr[a][b+1][c+1]=='P' and (arr[a][b][c+1]=='O' or arr[a][b+1][c]=='O'):
            return 0
        else:
            return 1
    for i in range(5):
        now=1
        for j in range(5):
            for k in range(5):
                if places[i][j][k]=='P':
                    now=lrtb(places,i,j,k)
                    if now==0:
                        answer.append(now)
                        break
                    now=lrtb2(places,i,j,k)
                    if now==0:
                        answer.append(now)
                        break
                    now=diagonal(places,i,j,k)
                    if now==0:
                        answer.append(now)
                        break
            if now==0:
                break
        if now==1:
            answer.append(now)
    return answer