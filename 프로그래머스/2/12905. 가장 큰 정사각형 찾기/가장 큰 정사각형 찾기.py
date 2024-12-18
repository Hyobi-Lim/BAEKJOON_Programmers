def solution(board):
    answer = 0
    for i in range(1,min(len(board),len(board[0]))):
        for j in range(i,len(board)):
            if board[j][i]==0:
                continue
            now=min(board[j-1][i],board[j][i-1],board[j-1][i-1])
            board[j][i]=now+1
        for j in range(i+1,len(board[0])):
            if board[i][j]==0:
                continue
            now=min(board[i-1][j],board[i][j-1],board[i-1][j-1])
            board[i][j]=now+1
    answer=max(map(max,board))
    answer**=2
    return answer