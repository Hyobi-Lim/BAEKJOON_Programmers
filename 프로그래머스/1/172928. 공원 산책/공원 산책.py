def solution(park, routes):
    answer = []
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j]=='S':
                answer.append(i)
                answer.append(j)
                break
    for i in routes:
        if i[0]=='N' and answer[0]-int(i[2])>=0:
            for j in range(int(i[2])):
                if park[answer[0]-j-1][answer[1]]=='X':
                    break
                if j==int(i[2])-1:
                    answer[0]-=int(i[2])
        elif i[0]=='S' and answer[0]+int(i[2])<len(park):
            for j in range(int(i[2])):
                if park[answer[0]+j+1][answer[1]]=='X':
                    break
                if j==int(i[2])-1:
                    answer[0]+=int(i[2])
        elif i[0]=='W' and answer[1]-int(i[2])>=0:
            for j in range(int(i[2])):
                if park[answer[0]][answer[1]-j-1]=='X':
                    break
                if j==int(i[2])-1:
                    answer[1]-=int(i[2])
        elif i[0]=='E' and answer[1]+int(i[2])<len(park[0]):
            for j in range(int(i[2])):
                if park[answer[0]][answer[1]+j+1]=='X':
                    break
                if j==int(i[2])-1:
                    answer[1]+=int(i[2])
    return answer