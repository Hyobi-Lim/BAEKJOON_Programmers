def solution(weights):
    answer = 0
    num=dict()
    for i in weights:
        if i in num:
            num[i]+=1
        else:
            num[i]=1
    for i in num:
        if num[i]>=2:
            answer+=(num[i]*(num[i]-1)//2)
        if i*1/2 in num:
            answer+=num[i]*num[i*1/2]
        if i*2/3 in num:
            answer+=num[i]*num[i*2/3]
        if i*3/4 in num:
            answer+=num[i]*num[i*3/4]
    return answer