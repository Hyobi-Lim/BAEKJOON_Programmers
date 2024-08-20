def solution(progresses, speeds):
    answer = []
    rest=[0]*len(progresses)
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]==0:
            rest[i]=(100-progresses[i])//speeds[i]
        else:
            rest[i]=(100-progresses[i])//speeds[i]+1
    now=rest[0]
    restall=1
    for i in range(1,len(rest)):
        if rest[i]>now:
            answer.append(restall)
            now=rest[i]
            restall=1
        else:
            restall+=1
        if i==len(rest)-1:
            answer.append(restall)
    return answer