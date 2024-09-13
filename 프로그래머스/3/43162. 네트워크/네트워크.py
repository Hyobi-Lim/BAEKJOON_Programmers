def solution(n, computers):
    answer = 0
    check=[1]*len(computers)
    stack=[]
    for i in range(len(computers)):
        for j in range(0,i+1):
            computers[i][j]=0
    for i in range(len(computers)):
        if check[i]==1:
            answer+=1
            check[i]=0
            stack.append(i)
            while(len(stack)):
                a=stack.pop()
                for j in range(a+1,len(computers)):
                    if computers[a][j]==1:
                        computers[a][j]=0
                        stack.append(j)
                        check[j]=0
                for j in range(a):
                    if computers[j][a]==1:
                        computers[j][a]=0
                        stack.append(j)
                        check[j]=0
    return answer