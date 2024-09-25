def solution(k, d):
    answer = 0
    for i in range(0,d+1,k):
        if int((d**2-i**2)**0.5)>=0:
            answer+=int((d**2-i**2)**0.5)//k
            answer+=1
    return answer