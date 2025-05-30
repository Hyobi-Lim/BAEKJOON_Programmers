import sys
bingo=[list(map(int,input().split())) for _ in range(5)]
call_num=[list(map(int,input().split())) for _ in range(5)]
bingo_dict=dict()
for i in range(5):
    for j in range(5):
        bingo_dict[bingo[i][j]]=[i,j]
check=False
for i in range(5):
    for j in range(5):
        x,y=bingo_dict[call_num[i][j]]
        bingo[x][y]=0
        cnt=0
        for k in range(5):
            if bingo[k]==[0,0,0,0,0]:
                cnt+=1
        for k in range(5):
            now=[]
            for l in range(5):
                now.append(bingo[l][k])
            if now==[0,0,0,0,0]:
                cnt+=1
        if [bingo[0][0],bingo[1][1],bingo[2][2],bingo[3][3],bingo[4][4]]==[0,0,0,0,0]:
                cnt+=1
        if [bingo[0][4],bingo[1][3],bingo[2][2],bingo[3][1],bingo[4][0]]==[0,0,0,0,0]:
                cnt+=1
        if cnt>=3:
            print(5*i+j+1)
            check=True
            break
    if check==True:
        break