def solution(rows, columns, queries):
    answer = []
    matrix=[]
    for i in range(rows):
        matrix.append([columns*i+j+1 for j in range(columns)])
    for i in queries:
        before=matrix[i[0]][i[1]-1]
        now=matrix[i[0]-1][i[1]-1]
        min=before
        for j in range(i[1]-1,i[3]):
            now=matrix[i[0]-1][j]
            matrix[i[0]-1][j]=before
            before=now
            if before<min:
                min=before
        for j in range(i[0],i[2]):
            now=matrix[j][i[3]-1]
            matrix[j][i[3]-1]=before
            before=now
            if before<min:
                min=before
        for j in range(i[3]-2,i[1]-2,-1):
            now=matrix[i[2]-1][j]
            matrix[i[2]-1][j]=before
            before=now
            if before<min:
                min=before
        for j in range(i[2]-2,i[0]-1,-1):
            now=matrix[j][i[1]-1]
            matrix[j][i[1]-1]=before
            before=now
            if before<min:
                min=before
        answer.append(min)
    return answer