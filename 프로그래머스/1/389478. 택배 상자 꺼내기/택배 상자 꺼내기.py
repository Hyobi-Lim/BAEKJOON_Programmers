def solution(n, w, num):
    answer = 0
    if w==1:
        answer=n-num+1
    elif n%w==0:
        answer=n//w-(num-1)//w
    else:
        answer=n//w-(num-1)//w
        col=0
        collist=[]
        for i in range((num-1)//w*w+1,(num-1)//w*w+1+w):
            collist.append(i)
        if (num-1)//w%2==1:
            collist.reverse()
        for i in range(len(collist)):
            if collist[i]==num:
                col=i
        lastlist=[]
        for i in range(n//w*w+1,n+1):
            lastlist.append(i)
        if n//w%2==1:
            lastlist.reverse()
            lastlist=[0]*(w-len(lastlist))+lastlist
        else:
            lastlist+=[0]*(w-len(lastlist))
        if lastlist[col]!=0:
            answer+=1
    return answer