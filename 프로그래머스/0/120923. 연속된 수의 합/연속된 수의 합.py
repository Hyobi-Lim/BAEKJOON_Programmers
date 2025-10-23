def solution(num, total):
    answer = []
    if num%2==1:
        number=total//num-num//2
        for i in range(num):
            answer.append(number)
            number+=1
    else:
        number=total//num-num//2+1
        for i in range(num):
            answer.append(number)
            number+=1
    return answer