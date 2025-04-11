import sys,heapq
n=int(sys.stdin.readline())
answer=[]
heapq.heapify(answer)
for i in range(n):
    now=int(sys.stdin.readline())
    if now>0:
        heapq.heappush(answer,-now)
    else:
        if len(answer)==0:
            print(0)
        else:
            print(heapq.heappop(answer)*-1)