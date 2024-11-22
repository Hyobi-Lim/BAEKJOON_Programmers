import heapq
def solution(n, k, enemy):
    answer = 0
    nomatter=enemy[:k]
    heapq.heapify(nomatter)
    rest=[]
    restsum=0
    for i in range(k,len(enemy)):
        if enemy[i]<=nomatter[0]:
            if enemy[i]+restsum<=n:
                rest.append(enemy[i])
                restsum+=enemy[i]
            else:
                break
        else:
            heapq.heappush(nomatter,enemy[i])
            new=heapq.heappop(nomatter)
            if new+restsum<=n:
                rest.append(new)
                restsum+=new
            else:
                break
    answer=len(nomatter)+len(rest)
    return answer