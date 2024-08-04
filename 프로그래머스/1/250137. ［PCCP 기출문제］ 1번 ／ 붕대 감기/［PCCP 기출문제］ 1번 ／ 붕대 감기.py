def solution(bandage, health, attacks):
    answer = health
    attacktime=[]
    for i in range(len(attacks)):
        attacktime.append(attacks[i][0])
    accumulation=0
    for i in range(1,attacktime[len(attacktime)-1]+1):
        accumulation+=1
        if i in attacktime:
            answer-=attacks[attacktime.index(i)][1]
            accumulation=0
        elif accumulation==bandage[0]:
            accumulation=0
            answer+=bandage[1]
            answer+=bandage[2]
        else:
            answer+=bandage[1]
        if answer>health:
            answer=health
        elif answer<=0:
            answer=-1
            break
    return answer