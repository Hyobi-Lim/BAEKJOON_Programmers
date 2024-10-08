def solution(x, y, n):
    answer = -1
    turn=0
    dp={x}
    while(len(dp)!=0):
        if answer!=-1:
            break
        new=set()
        for i in dp:
            if i==y:
                answer=turn
                break
            else:
                if i+n<=y:
                    new.add(i+n)
                if i*2<=y:
                    new.add(i*2)
                if i*3<=y:
                    new.add(i*3)
        dp=new
        turn+=1
    return answer