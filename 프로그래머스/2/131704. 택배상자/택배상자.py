def solution(order):
    answer = 0
    now=[]
    second=[]
    for i in range(1,len(order)+1):
        if order[len(now)]==i:
            now.append(i)
            answer+=1
        elif i<order[len(now)]:
            second.append(i)
        while(len(second)!=0 and second[len(second)-1]==order[len(now)]):
            now.append(second.pop())
            answer+=1
    return answer