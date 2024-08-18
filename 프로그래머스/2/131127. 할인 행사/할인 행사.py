def solution(want, number, discount):
    answer = 0
    li=[]
    for i in range(len(want)):
        li+=[want[i]]*number[i]
    li.sort()
    numbersum=sum(number)
    for i in range(len(discount)-numbersum+1):
        new=discount[i:i+numbersum]
        new.sort()
        if li==new:
            answer+=1
    return answer