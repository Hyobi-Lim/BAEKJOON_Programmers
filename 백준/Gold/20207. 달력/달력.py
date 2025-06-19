import sys
n=int(sys.stdin.readline())
schedule=dict()
for i in range(n):
    start,end=map(int,sys.stdin.readline().split())
    for j in range(start,end+1):
        schedule[j]=schedule.get(j,0)+1
sequence=0
max_schedule=0
answer=0
for i in range(1,366):
    if i not in schedule:
        answer+=sequence*max_schedule
        sequence=0
        max_schedule=0
    else:
        sequence+=1
        if max_schedule<schedule[i]:
            max_schedule=schedule[i]
if sequence!=0:
    answer+=sequence*max_schedule
print(answer)