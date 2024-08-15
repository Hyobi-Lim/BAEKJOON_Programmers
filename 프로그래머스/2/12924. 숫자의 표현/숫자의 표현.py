def solution(n):
    answer = 0
    front=0
    back=1
    while(True):
        if front==n-1 and back==n:
            answer+=1
            break
        if back*(back+1)-front*(front+1)==n*2:
            answer+=1
            back+=1
        elif back*(back+1)-front*(front+1)>n*2:
            front+=1
        else:
            back+=1
    return answer