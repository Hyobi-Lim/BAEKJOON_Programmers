def solution(queue1, queue2):
    answer = -1
    queue=queue1+queue2
    start=0
    end=0
    sum_num=queue[0]
    half_num=sum(queue)//2
    while(start<len(queue)):
        if sum_num<half_num:
            if(end==len(queue)-1):
                break
            end+=1
            sum_num+=queue[end]
        elif sum_num>half_num:
            sum_num-=queue[start]
            start+=1
        else:
            cnt=0
            if(start==0 and end<len(queue1)-1):
                cnt=end+1+len(queue2)
            elif(end<len(queue1)-1):
                cnt=start+end+1+len(queue2)
            elif(end==len(queue1)-1):
                cnt=start
            elif(start==0 and len(queue1)<=end<len(queue)-1):
                cnt=end-len(queue1)+1
            elif(0<start<len(queue1) and len(queue1)<=end<len(queue)-1):
                cnt=start+end-len(queue1)+1
            elif(0<start<len(queue1) and end==len(queue)-1):
                cnt=start+len(queue1)
            elif(start==len(queue1) and end<len(queue)-1):
                cnt=end+1
            elif(start>len(queue1) and end<len(queue)-1):
                cnt=start+end+1-len(queue1)
            elif(start>len(queue1) and end==len(queue)-1):
                cnt=start-len(queue1)+1
            if(answer==-1 or answer>cnt):
                answer=cnt
            if(end==len(queue)-1):
                break
            end+=1
            sum_num+=queue[end]
            sum_num-=queue[start]
            start+=1
    return answer