def solution(a, b):
    answer = ''
    num=0
    month=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    day=['THU','FRI','SAT','SUN','MON','TUE','WED']
    for i in range(a):
        num+=month[i]
    num+=b
    answer=day[num%7]
    return answer