def solution(friends, gifts):
    answer = 0
    givetake=[[0]*len(friends) for _ in range(len(friends))]
    giftscore=[0]*len(friends)
    friendsindex={}
    nowgift={}
    for i in range(len(friends)):
        friendsindex[friends[i]]=i
        nowgift[friends[i]]=0
    for i in gifts:
        now=i.split()
        givetake[friendsindex[now[0]]][friendsindex[now[1]]]+=1
    for i in range(len(giftscore)):
        row=0
        col=0
        for j in range(len(giftscore)):
            row+=givetake[i][j]
            col+=givetake[j][i]
        giftscore[i]=row-col
    for i in range(len(friends)):
        for j in range(i+1,len(friends)):
            if givetake[i][j]>givetake[j][i]:
                nowgift[friends[i]]+=1
            elif givetake[i][j]<givetake[j][i]:
                nowgift[friends[j]]+=1
            else:
                if giftscore[i]>giftscore[j]:
                    nowgift[friends[i]]+=1
                elif giftscore[i]<giftscore[j]:
                    nowgift[friends[j]]+=1
    for i in friends:
        if nowgift[i]>answer:
            answer=nowgift[i]
    return answer