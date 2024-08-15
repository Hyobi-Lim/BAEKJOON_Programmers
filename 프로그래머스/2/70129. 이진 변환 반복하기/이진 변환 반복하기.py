def solution(s):
    answer = [0,0]
    while(s!='1'):
        answer[0]+=1
        zerocount=s.count('0')
        answer[1]+=zerocount
        s=str(format((len(s)-zerocount),'b'))
    return answer