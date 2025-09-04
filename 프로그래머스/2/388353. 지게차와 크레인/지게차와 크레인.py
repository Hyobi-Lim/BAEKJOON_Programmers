def new_outline(storage):
    stack=[]
    visited=[[False]*len(storage[0]) for _ in range(len(storage))]
    r=[0,-1,0,1]
    c=[-1,0,1,0]
    for i in range(len(storage[0])):
        stack.append([0,i])
        stack.append([len(storage)-1,i])
        visited[0][i]=True
        visited[len(storage)-1][i]=True
    for i in range(len(storage)):
        stack.append([i,0])
        stack.append([i,len(storage[0])-1])
        visited[i][0]=True
        visited[i][len(storage[0])-1]=True
    while(stack):
        now_x,now_y=stack.pop()
        if(storage[now_x][now_y]!=" "):
            continue
        for i in range(4):
            new_x=now_x+r[i]
            new_y=now_y+c[i]
            if(0<=new_x<len(storage) and 0<=new_y<len(storage[0]) and visited[new_x][new_y]==False):
                visited[new_x][new_y]=True
                if(storage[new_x][new_y]==" "):
                    stack.append([new_x,new_y])
    return visited
def solution(storage, requests):
    answer = 0
    outline=[[False]*len(storage[0]) for _ in range(len(storage))]
    for i in range(len(storage[0])):
        outline[0][i]=True
        outline[len(storage)-1][i]=True
    for i in range(len(storage)):
        storage[i]=list(storage[i])
        outline[i][0]=True
        outline[i][len(storage[0])-1]=True
    for i in requests:
        if len(i)==2:
            for j in range(len(storage)):
                for k in range(len(storage[0])):
                    if storage[j][k]==i[0]:
                        storage[j][k]=" "
        else:
            outline=new_outline(storage)
            for j in range(len(storage)):
                for k in range(len(storage[0])):
                    if storage[j][k]==i[0] and outline[j][k]:
                        storage[j][k]=" "
    for i in range(len(storage)):
        for j in range(len(storage[0])):
            if storage[i][j]!=" ":
                answer+=1
    return answer