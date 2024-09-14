def solution(dirs):
    answer = 0
    now=[0,0]
    all=[]
    for i in dirs:
        new=now[:]
        if i=='U':
            new[1]+=1
        if i=='D':
            new[1]-=1
        if i=='R':
            new[0]+=1
        if i=='L':
            new[0]-=1
        if new[0]<-5 or new[1]<-5 or new[0]>5 or new[1]>5:
            continue
        if now+new in all or new+now in all:
            now=new
            continue
        all.append(now+new)
        now=new
    answer=len(all)
    return answer