def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]==1:
                for a in range(-1,2):
                    for b in range(-1,2):
                        if 0<=i+a<len(board) and 0<=j+b<len(board) and board[i+a][j+b]==0:
                            board[i+a][j+b]=2    
    for i in range(len(board)):
        answer+=board[i].count(0)
    return answer