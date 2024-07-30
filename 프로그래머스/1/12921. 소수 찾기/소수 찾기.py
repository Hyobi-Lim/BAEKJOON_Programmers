def solution(n):
    answer = 1
    for i in range(3,n+1,2):
        num=0
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                num+=1
                break
        if num==0:
            answer+=1
    return answer