def solution(N, stages):
    answer = []
    fail=[]
    stages.sort()
    for i in range(1,N+1):
        if i in stages:
            fail.append(stages.count(i)/(len(stages)-stages.index(i)))
        else:
            fail.append(0)
    failsort=fail[:]
    failsort.sort(reverse=True)
    for i in failsort:
        answer.append(fail.index(i)+1)
        fail[fail.index(i)]=-1
    return answer