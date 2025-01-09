def solution(m, musicinfos):
    answer = '(None)'
    splitm=[]
    all=[]
    for i in range(len(m)):
        if m[i]=='#':
            splitm[len(splitm)-1]+='#'
        else:
            splitm.append(m[i])
    for i in musicinfos:
        now=i.split(',')
        for j in range(2):
            now[j]=now[j].split(':')
            now[j][0]=int(now[j][0])
            now[j][1]=int(now[j][1])
        time=(now[1][0]-now[0][0])*60+(now[1][1]-now[0][1])
        music=[]
        for j in range(len(now[3])):
            if now[3][j]=='#':
                music[len(music)-1]+='#'
            else:
                music.append(now[3][j])
        play=music*(time//len(music))+music[:time%len(music)]
        if len(play)>=len(splitm):
            for j in range(len(play)-len(splitm)+1):
                if play[j:j+len(splitm)]==splitm:
                    all.append([time,now[2]])
                    break
    if len(all)!=0:
        all=sorted(all,key=lambda x:x[0],reverse=True)
        answer=all[0][1]
    return answer