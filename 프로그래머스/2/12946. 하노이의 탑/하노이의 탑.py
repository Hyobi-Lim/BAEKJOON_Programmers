def solution(n):
    answer = []
    def hanoi(num,fromblock,toblock,midblock):
        if num==1:
            answer.append([fromblock,toblock])
            return
        hanoi(num-1,fromblock,midblock,toblock)
        answer.append([fromblock,toblock])
        hanoi(num-1,midblock,toblock,fromblock)
    hanoi(n,1,3,2)
    return answer