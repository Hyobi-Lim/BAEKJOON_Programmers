def solution(line):
    answer = []
    coordinate=set()
    min_x=float("inf")
    max_x=float("-inf")
    min_y=float("inf")
    max_y=float("-inf")
    for i in range(len(line)):
        for j in range(i+1,len(line)):
            x=0
            y=0
            new_i=line[i][:]
            new_j=line[j][:]
            for k in range(3):
                new_i[k]*=line[j][0]
                new_j[k]*=line[i][0]
            if new_i[1]-new_j[1]==0 and -(new_i[2]-new_j[2])==0:
                y=0
            elif new_i[1]-new_j[1]!=0 and -(new_i[2]-new_j[2])%(new_i[1]-new_j[1])==0:
                y=-(new_i[2]-new_j[2])//(new_i[1]-new_j[1])
            else:
                continue
            if line[i][0]==0 and -(line[i][1]*y+line[i][2])==0 and -(line[j][1]*y+line[j][2])%line[j][0]==0:
                x=-(line[j][1]*y+line[j][2])//line[j][0]
            elif line[i][0]!=0 and -(line[i][1]*y+line[i][2])%line[i][0]==0:
                x=-(line[i][1]*y+line[i][2])//line[i][0]
            else:
                continue
            if max_x<x:
                max_x=x
            if min_x>x:
                min_x=x
            if max_y<y:
                max_y=y
            if min_y>y:
                min_y=y
            coordinate.add((x,y))
    if len(coordinate)==1:
        answer.append("*")
    else:
        answer=[['.']*(max_x-min_x+1) for _ in range(max_y-min_y+1)]
        for i in coordinate:
            now_x,now_y=i
            answer[max_y-now_y][now_x-min_x]='*'
        for i in range(max_y-min_y+1):
            answer[i]=''.join(answer[i])
    return answer