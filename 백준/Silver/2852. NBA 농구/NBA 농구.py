import sys
n=int(sys.stdin.readline())
score=[0,0]
score_time=[0,0]
bf_team=0
for i in range(n):
    now=list(sys.stdin.readline().split())
    now[1]=now[1].split(':')
    if score[0]>score[1]:
        score_time[0]+=int(now[1][0])*60+int(now[1][1])-int(bf_team[1][0])*60-int(bf_team[1][1])
    elif score[0]<score[1]:
        score_time[1]+=int(now[1][0])*60+int(now[1][1])-int(bf_team[1][0])*60-int(bf_team[1][1])
    bf_team=now
    if int(now[0])==1:
        score[0]+=1
    else:
        score[1]+=1
    if i==n-1:
        if score[0]>score[1]:
            score_time[0]+=48*60-int(bf_team[1][0])*60-int(bf_team[1][1])
        elif score[0]<score[1]:
            score_time[1]+=48*60-int(bf_team[1][0])*60-int(bf_team[1][1])
print(f"{score_time[0]//60:02d}:{score_time[0]-score_time[0]//60*60:02d}")
print(f"{score_time[1]//60:02d}:{score_time[1]-score_time[1]//60*60:02d}")