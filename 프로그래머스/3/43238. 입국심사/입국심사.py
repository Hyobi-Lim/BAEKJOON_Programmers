def solution(n, times):
    def checking(left,right,n,times):
        nonlocal answer
        if left>right:
            return
        mid=(left+right)//2
        allnum=0
        for i in range(len(times)):
            allnum+=(mid//times[i])
        if allnum>=n:
            answer=mid
            checking(left,mid-1,n,times)
        else:
            checking(mid+1,right,n,times)
    answer = max(times)*n
    checking(1,max(times)*n,n,times)
    return answer