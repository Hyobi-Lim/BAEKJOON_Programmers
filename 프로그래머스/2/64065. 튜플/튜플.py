def solution(s):
    answer = []
    s=s[1:len(s)-1].replace('{','').split(',')
    alls=[]
    now=[]
    for i in s:
        if '}' in i:
            nowstr=i[:len(i)-1]
            now.append(int(nowstr))
            alls.append(now)
            now=[]
        else:
            now.append(int(i))
    alls=sorted(alls, key=lambda x: len(x))
    for i in alls:
        for j in i:
            if j not in answer:
                answer.append(j)
                break
    return answer