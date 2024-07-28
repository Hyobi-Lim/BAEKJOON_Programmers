def solution(n, lost, reserve):
    answer = n-len(lost)
    lost.sort()
    reserve.sort()
    for i in range(len(lost)):
        if lost[i] in reserve:
            answer+=1
            reserve[reserve.index(lost[i])]=-10
            lost[i]=-10
    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            answer+=1
            reserve[reserve.index(lost[i]-1)]=-10
            lost[i]=-10
        elif lost[i]+1 in reserve:
            answer+=1
            reserve[reserve.index(lost[i]+1)]=-10
            lost[i]=-10
    return answer