def solution(board, moves):
    answer = 0
    nowdoll=[]
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1]!=0:
                if len(nowdoll)==0:
                    nowdoll.append(board[j][i-1])
                else:
                    if nowdoll[len(nowdoll)-1]==board[j][i-1]:
                        answer+=2
                        nowdoll.pop()
                    else:
                        nowdoll.append(board[j][i-1])
                board[j][i-1]=0
                break
    return answer