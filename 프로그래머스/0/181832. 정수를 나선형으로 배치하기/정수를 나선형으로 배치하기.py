def solution(n):
    answer = [[0]*n for _ in range(n)]
    l=[0,1,0,-1]
    r=[1,0,-1,0]
    lnum=0
    rnum=0
    nl=0
    nr=0
    for i in range(1,n*n+1):
        answer[nl][nr]=i
        if nr+r[rnum%4]<0 or nr+r[rnum%4]>=n or nl+l[lnum%4]<0 or nl+l[lnum%4]>=n or answer[nl+l[lnum%4]][nr+r[rnum%4]]!=0:
            lnum+=1
            rnum+=1
        nl+=l[lnum%4]
        nr+=r[rnum%4]
    return answer