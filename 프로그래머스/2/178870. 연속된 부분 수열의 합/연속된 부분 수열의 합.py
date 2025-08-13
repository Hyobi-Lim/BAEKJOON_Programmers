def solution(sequence, k):
    answer = []
    start=0
    end=0
    now_sum=sequence[0]
    while(start<len(sequence)):
        if(now_sum<k):
            if(end==len(sequence)-1):
                break
            end+=1
            now_sum+=sequence[end]
        elif(now_sum>k):
            now_sum-=sequence[start]
            start+=1
        else:
            if(len(answer)==0):
                answer=[start,end]
            else:
                if(end-start<answer[1]-answer[0]):
                    answer=[start,end]
            if(end==len(sequence)-1):
                break
            end+=1
            now_sum+=sequence[end]
            now_sum-=sequence[start]
            start+=1
    return answer