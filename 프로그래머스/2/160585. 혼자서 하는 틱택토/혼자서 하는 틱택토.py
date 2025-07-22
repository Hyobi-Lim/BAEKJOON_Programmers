def solution(board):
    answer = 0
    first_move=0
    second_move=0
    for i in range(3):
        board[i]=list(board[i])
        for j in range(3):
            if board[i][j]=='O':
                first_move+=1
            elif board[i][j]=='X':
                second_move+=1
    def bingo(arr,sign):
        result=False
        for i in range(3):
            if arr[i][0]==sign and arr[i][1]==sign and arr[i][2]==sign:
                result=True
                break
            if arr[0][i]==sign and arr[1][i]==sign and arr[2][i]==sign:
                result=True
                break
        if arr[0][0]==sign and arr[1][1]==sign and arr[2][2]==sign:
            result=True
        if arr[0][2]==sign and arr[1][1]==sign and arr[2][0]==sign:
            result=True
        return result
    if first_move==second_move:
        if first_move<=2:
            answer=1
        else:
            first_bingo=bingo(board,"O")
            second_bingo=bingo(board,"X")
            if first_bingo==False:
                answer=1
    elif first_move==second_move+1:
        if first_move<=3:
            answer=1
        else:
            first_bingo=bingo(board,"O")
            second_bingo=bingo(board,"X")
            if second_bingo==False:
                answer=1
    return answer