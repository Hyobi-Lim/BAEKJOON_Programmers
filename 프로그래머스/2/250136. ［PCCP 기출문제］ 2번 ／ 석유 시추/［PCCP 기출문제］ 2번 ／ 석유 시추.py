import sys
sys.setrecursionlimit(10**9)
def solution(land):
    dr=[0,1,0,-1,]
    dc=[1,0,-1,0]
    count=0
    def changealp(land,alp,r,c):
        nonlocal count
        land[r][c]=alp
        count+=1
        for i in range(4):
            if r+dr[i]<0 or r+dr[i]>=len(land) or c+dc[i]<0 or c+dc[i]>=len(land[0]):
                continue
            elif land[r+dr[i]][c+dc[i]]==1:
                changealp(land,alp,r+dr[i],c+dc[i])
    num=2
    oildict=dict()
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j]==1:
                count=0
                changealp(land,str(num),i,j)
                oildict[str(num)]=count
                num+=1
    answer = 0
    for i in range(len(land[0])):
        now=set()
        for j in range(len(land)):
            if land[j][i]!=0:
                now.add(land[j][i])
        alloil=0
        for j in now:
            alloil+=oildict[j]
        if answer==0 or answer<alloil:
            answer=alloil
    return answer