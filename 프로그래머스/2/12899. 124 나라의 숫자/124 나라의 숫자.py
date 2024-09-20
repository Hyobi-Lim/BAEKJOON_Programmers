def solution(n):
    answer = ''
    all=[]
    while(n>0):
        if n%3==0:
            all.append('4')
            n//=3
            n-=1
        elif n%3==2:
            all.append('2')
            n//=3
        elif n%3==1:
            all.append('1')
            n//=3
    for i in range(len(all)-1,-1,-1):
        answer+=all[i]
    return answer