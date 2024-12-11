def solution(picks, minerals):
    def check(restpicks,restminerals,fatigue,count):
        nonlocal answer
        if sum(restpicks)==0 or len(restminerals)==0:
            if count<answer or answer==0:
                answer=count
            return
        for i in range(3):
            if restpicks[i]==0:
                continue
            else:
                newrestpicks=restpicks[:]
                newrestpicks[i]-=1
                newrestminerals=restminerals[:]
                num=count
                for j in range(5):
                    if len(newrestminerals)==0:
                        if num<answer or answer==0:
                            answer=num
                        return
                    else:                            
                        num+=fatigue[i][newrestminerals[0]]
                        del newrestminerals[0]
                        if j==4:
                            check(newrestpicks,newrestminerals,fatigue,num)
    answer = 0
    fatigue=[{"diamond":1,"iron":1,"stone":1},{"diamond":5,"iron":1,"stone":1},{"diamond":25,"iron":5,"stone":1}]
    check(picks,minerals,fatigue,0)
    return answer