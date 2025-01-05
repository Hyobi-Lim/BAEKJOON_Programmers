def solution(n):
    answer = []
    answerdiv=[[0]*(i+1) for i in range(n)]
    num=n-1
    numcount=[0,0]
    now=[0,0]
    for i in range(1,n*(n+1)//2+1):
        answerdiv[now[0]][now[1]]=i
        numcount[0]+=1
        if numcount[1]==0 and numcount[0]==num+1:
            numcount[0]=0
            numcount[1]+=1
        elif numcount[1]==1 and numcount[0]==num:
            numcount[0]=0
            numcount[1]+=1
        elif numcount[1]==2 and numcount[0]==num-1:
            numcount[0]=0
            numcount[1]+=1
        if numcount[1]==3:
            num-=3
            numcount=[0,0]
            now[0]+=1
            continue
        if numcount[1]==0:
            now[0]+=1
        elif numcount[1]==1:
            now[1]+=1
        else:
            now[0]-=1
            now[1]-=1
    for i in range(len(answerdiv)):
        answer+=answerdiv[i]
    return answer