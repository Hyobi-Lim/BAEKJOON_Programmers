import heapq
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while(scoville[0]<K):
        if len(scoville)==1:
            answer=-1
            break
        result = heapq.heappop(scoville)+heapq.heappop(scoville)*2
        heapq.heappush(scoville,result)
        answer+=1
    return answer