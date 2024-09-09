def solution(m, n, puddles):
    all=[[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if (i==0 and j==0) or [j+1,i+1] in puddles:
                all[i][j]=0
            elif i==0:
                if j-1!=0 and all[i][j-1]==0:
                    all[i][j]=0
                else:
                    all[i][j]=1
            elif j==0:
                if i-1!=0 and all[i-1][j]==0:
                    all[i][j]=0
                else:
                    all[i][j]=1
            else:
                all[i][j]=all[i][j-1]+all[i-1][j]
    answer=all[n-1][m-1]%1000000007
    return answer