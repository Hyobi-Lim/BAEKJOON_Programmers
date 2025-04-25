import sys,math
n=int(sys.stdin.readline())
cookie=[]
herat=[]
answer=[0,0,0,0,0]
for i in range(n):
    cookie.append(list(sys.stdin.readline().strip()))
for i in range(1,n-1):
    for j in range(1,n-1):
        if cookie[i][j]=='*' and cookie[i+1][j]=='*' and cookie[i][j+1]=='*' and cookie[i-1][j]=='*' and cookie[i][j-1]=='*':
            heart=[i,j]
print(heart[0]+1,heart[1]+1)
for i in range(heart[1]-1,-1,-1):
    if cookie[heart[0]][i]=='*':
        answer[0]+=1
    else:
        break
for i in range(heart[1]+1,n):
    if cookie[heart[0]][i]=='*':
        answer[1]+=1
    else:
        break
for i in range(heart[0]+1,n):
    if cookie[i][heart[1]]=='*':
        answer[2]+=1
    else:
        heart[0]=i
        break
for i in range(heart[0],n):
    if cookie[i][heart[1]-1]=='*':
        answer[3]+=1
    else:
        break
for i in range(heart[0],n):
    if cookie[i][heart[1]+1]=='*':
        answer[4]+=1
    else:
        break
print(*answer)