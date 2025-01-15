import math
def solution(diffs, times, limit):
    answer = 0
    times_sum=sum(times)
    for i in range(len(times)-1,0,-1):
        times[i]+=times[i-1]
    diffs_times=[]
    for i in range(len(diffs)):
        diffs_times.append([diffs[i],times[i]])
    diffs_times=sorted(diffs_times,key=lambda x:x[0])
    diffs_times_key=[times_sum]*len(diffs_times)
    diffs_times_value=[0]*len(diffs_times)
    for i in range(len(diffs_times)-2,-1,-1):
        diffs_times_key[i]=diffs_times[i+1][1]*diffs_times[i+1][0]+diffs_times_key[i+1]
        diffs_times_value[i]=diffs_times[i+1][1]+diffs_times_value[i+1]
    for i in range(len(diffs)):
        if i==len(diffs)-1:
            if diffs_times_key[i]<=limit and (answer==0 or answer>diffs_times[i][0]):
                answer=diffs_times[i][0]
        else:
            new_limit=math.ceil((diffs_times_key[i]-limit)/diffs_times_value[i])
            new_min=0
            if new_limit>=diffs_times[i+1][0]:
                continue
            elif new_limit<=diffs_times[i][0]:
                new_min=diffs_times[i][0]
            else:
                new_min=new_limit
            if answer==0 or answer>new_min:
                answer=new_min
    return answer