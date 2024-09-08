def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if i==1:
                triangle[i][j]+=triangle[0][0]
            elif j==0:
                triangle[i][0]+=triangle[i-1][0]
            elif j==len(triangle[i])-1:
                triangle[i][j]+=triangle[i-1][j-1]
            else:
                if triangle[i-1][j-1]>triangle[i-1][j]:
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=triangle[i-1][j]
    answer=max(triangle[len(triangle)-1])
    return answer