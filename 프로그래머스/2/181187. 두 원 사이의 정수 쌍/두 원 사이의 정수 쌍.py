import math
def solution(r1, r2):
    answer = 0
    for i in range(r2):
        if i>=r1:
            numr1=1
        else:
            numr1=math.ceil(math.sqrt(r1**2-i**2))
        numr2=math.floor(math.sqrt(r2**2-i**2))
        answer+=(numr2-numr1+1)
    answer*=4
    return answer