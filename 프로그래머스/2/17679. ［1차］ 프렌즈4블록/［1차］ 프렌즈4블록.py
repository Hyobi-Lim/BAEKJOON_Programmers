from copy import deepcopy
def solution(m, n, board):
    answer = 0
    while(1):
        for i in range(m):
            board[i]=list(board[i])
        new=deepcopy(board)
        for i in range(m-1):
            for j in range(n-1):
                if board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1] and board[i][j]!=' ':
                    new[i][j]='a'
                    new[i+1][j]='a'
                    new[i][j+1]='a'
                    new[i+1][j+1]='a'
        count=0
        for i in range(m):
            for j in range(n):
                if new[i][j]=='a':
                    answer+=1
                    count+=1
                    for k in range(i,0,-1):
                        new[k][j]=new[k-1][j]
                    new[0][j]=' '
        board=new
        if count==0:
            break
    return answer