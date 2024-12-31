def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        if i==1:
            answer.append(0)
        else:
            num=1
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    if i//j<=10**7:
                        num=i//j
                        break
                    else:
                        num=j
            answer.append(num)
    return answer