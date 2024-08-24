def solution(n,a,b):
    answer = 0
    now=[i for i in range(1,n+1)]
    checknum=0
    while(checknum==0):
        new=[]
        for i in range(0,len(now),2):
            if (now[i]==a and now[i+1]==b) or (now[i]==b and now[i+1]==a):
                checknum=1
                break
            elif now[i]==a or now[i+1]==a:
                new.append(a)
            elif now[i]==b or now[i+1]==b:
                new.append(b)
            else:
                new.append(now[i])
        now=new
        answer+=1
    return answer