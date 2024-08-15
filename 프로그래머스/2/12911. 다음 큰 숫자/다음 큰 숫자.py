def solution(n):
    answer = n+1
    while(True):
        if str(format(n,'b')).count('1')==str(format(answer,'b')).count('1'):
            break
        else:
            answer+=1
    return answer