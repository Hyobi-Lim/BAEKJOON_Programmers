import math
def solution(number, limit, power):
    answer = 0
    for i in range(1,number+1):
        num=0
        for j in range(1,math.ceil(i**0.5)):
            if i%j==0:
                num+=1
        num*=2
        if math.ceil(i**0.5)==int(i**0.5):
            num+=1
        if num<=limit:
            answer+=num
        else:
            answer+=power
    return answer