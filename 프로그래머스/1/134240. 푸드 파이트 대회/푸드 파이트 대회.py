def solution(food):
    answer = ''
    for i in range(1,len(food)):
        answer+=(str(i)*(food[i]//2))
    reverseanswer=answer[::-1]
    return answer+'0'+reverseanswer