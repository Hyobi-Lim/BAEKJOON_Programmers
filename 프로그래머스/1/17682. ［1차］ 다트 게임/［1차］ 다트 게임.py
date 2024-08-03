def solution(dartResult):
    answer = []
    num=['1','2','3','4','5','6','7','8','9']
    for i in range(len(dartResult)):
        if dartResult[i]=='S':
            answer[len(answer)-1]**=1
        elif dartResult[i]=='D':
            answer[len(answer)-1]**=2
        elif dartResult[i]=='T':
            answer[len(answer)-1]**=3
        elif dartResult[i]=='*':
            if len(answer)==1:
                answer[0]*=2
            else:
                answer[len(answer)-1]*=2
                answer[len(answer)-2]*=2
        elif dartResult[i]=='#':
            answer[len(answer)-1]*=(-1)
        elif dartResult[i] in num:
            answer.append(int(dartResult[i]))
        elif dartResult[i]=='0':
            if i!=0 and dartResult[i-1] in num:
                answer[len(answer)-1]=10
            else:
                answer.append(int(dartResult[i]))
    return sum(answer)