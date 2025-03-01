import sys
import heapq
n=int(sys.stdin.readline())
hip=[]
hip_dict=dict()
heapq.heapify(hip)
for i in range(n):
    num=int(sys.stdin.readline())
    if num!=0:
        heapq.heappush(hip,abs(num))
        if num in hip_dict:
            hip_dict[num]+=1
        else:
            hip_dict[num]=1
    else:
        if len(hip)==0:
            print(0)
        else:
            now_num=heapq.heappop(hip)
            if -now_num in hip_dict:
                print(-now_num)
                if hip_dict[-now_num]==1:
                    del hip_dict[-now_num]
                else:
                    hip_dict[-now_num]-=1
            else:
                print(now_num)
                if hip_dict[now_num]==1:
                    del hip_dict[now_num]
                else:
                    hip_dict[now_num]-=1