def solution(mats, park):
    answer = 0
    mats.sort(reverse=True)
    for i in mats:
        for j in range(len(park)-i+1):
            for k in range(len(park[0])-i+1):
                now=[]
                for l in range(i):
                    now+=park[j+l][k:k+i]
                if now.count('-1')==len(now):
                    answer=i
                    break
            if answer!=0:
                break
        if answer!=0:
            break
    if answer==0:
        answer=-1
    return answer