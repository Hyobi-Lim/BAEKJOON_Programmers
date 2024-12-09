def solution(k, ranges):
    answer = []
    xy=[0.0,k]
    num=k
    while(num!=1):
        if num%2==0:
            num//=2
        else:
            num*=3
            num+=1
        xy.append(num)
    for i in range(1,len(xy)-1):
        xy[i]=(xy[i]+xy[i+1])/2
        xy[i]=(xy[i]+xy[i-1])
    xy.pop()
    for i in range(len(ranges)):
        ranges[i][1]+=(len(xy)-1)
        if ranges[i][1]-ranges[i][0]<0:
            answer.append(-1)
        else:
            answer.append(xy[ranges[i][1]]-xy[ranges[i][0]])
    return answer