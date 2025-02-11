def solution(schedules, timelogs, startday):
    answer = len(schedules)
    for i in range(len(schedules)):
        late_timelogs=schedules[i]+10
        if late_timelogs%100>59:
            late_timelogs+=40
        for j in range(startday,startday+7):
            if j%7==6 or j%7==0:
                continue
            else:
                if timelogs[i][j-startday]>late_timelogs:
                    answer-=1
                    break
    return answer