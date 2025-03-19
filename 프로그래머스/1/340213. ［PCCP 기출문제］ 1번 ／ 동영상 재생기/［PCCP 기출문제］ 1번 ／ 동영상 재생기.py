def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len=video_len.split(":")
    video_len=list(map(int,video_len))
    pos=pos.split(":")
    pos=list(map(int,pos)) 
    op_start=op_start.split(":")
    op_start=list(map(int,op_start)) 
    op_end=op_end.split(":")
    op_end=list(map(int,op_end))
    if op_start[0]<pos[0] or (op_start[0]==pos[0] and op_start[1]<=pos[1]):
        if op_end[0]>pos[0] or (op_end[0]==pos[0] and op_end[1]>=pos[1]):
            pos=op_end[:]
    for i in commands:
        if i=="prev":
            if pos[0]==0 and pos[1]<=10:
                pos=[0,0]
            else:
                if pos[1]<10:
                    pos[0]-=1
                    pos[1]+=50
                else:
                    pos[1]-=10
        else:
            pos[1]+=10
            if pos[1]>=60:
                pos[0]+=1
                pos[1]-=60
            if pos[0]>video_len[0] or (pos[0]==video_len[0] and pos[1]>video_len[1]):
                pos=video_len[:]
        if op_start[0]<pos[0] or (op_start[0]==pos[0] and op_start[1]<=pos[1]):
            if op_end[0]>pos[0] or (op_end[0]==pos[0] and op_end[1]>=pos[1]):
                pos=op_end[:]
    if pos[0]<10:
        pos[0]='0'+str(pos[0])
    if pos[1]<10:
        pos[1]='0'+str(pos[1])
    answer=str(pos[0])+':'+str(pos[1])
    return answer