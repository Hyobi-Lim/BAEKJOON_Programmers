import sys
r,c=map(int,sys.stdin.readline().split())
island=[list(sys.stdin.readline().strip()) for _ in range(r)]
island_check=set()
for i in range(r):
    for j in range(c):
        if island[i][j]=='X':
            num=0
            if i==0 or island[i-1][j]=='.':
                num+=1
            if j==0 or island[i][j-1]=='.':
                num+=1
            if i+1==r or island[i+1][j]=='.':
                num+=1
            if j+1==c or island[i][j+1]=='.':
                num+=1
            if num>=3:
                island_check.add((i,j))
for i in island_check:
    x,y=i
    island[x][y]='.'
for i in range(r-1,-1,-1):
    if island[i]==['.']*c:
        island.pop()
    else:
        break
r=len(island)
for i in range(r):
    if island[i]!=['.']*c:
        island=island[i:]
        break
r=len(island)
check=False
for i in range(c-1,-1,-1):
    for j in range(r):
        if island[j][i]!='.':
            check=True
            break
        if j+1==r:
            for j in range(r):
                island[j].pop()
    if check==True:
        break
c=len(island[0])
check=False
for i in range(c):
    for j in range(r):
        if island[j][i]!='.':
            check=True
            break
    if check==True:
        for j in range(r):
            island[j]=island[j][i:]
        break
for i in island:
    print(''.join(i))