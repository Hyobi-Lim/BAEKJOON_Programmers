def solution(n):
    answer = 0
    now={1:1,2:1}
    targetnum=1
    while(len(now)!=0):
        if targetnum==n:
            answer+=(now[n]%1000000007)
            break
        else:
            now[targetnum+1]+=now[targetnum]
            now[targetnum+2]=now[targetnum]
            del now[targetnum]
            targetnum+=1
    return answer