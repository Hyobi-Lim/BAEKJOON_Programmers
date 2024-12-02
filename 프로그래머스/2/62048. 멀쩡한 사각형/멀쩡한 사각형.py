import math
def solution(w,h):
    answer = w*h
    if w==1 or h==1:
        return 0
    maxdiv=math.gcd(w,h)
    eachno=[]
    checknum=w//maxdiv
    for i in range(checknum):
        now=math.ceil(h/w*(i+1))-math.floor(h/w*i)
        if i<w%maxdiv:
            answer-=now*((w//checknum)+1)
        else:
            answer-=now*(w//checknum)
    return answer