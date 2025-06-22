import sys
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(19)]
answer=0
answer_index=[0,0]
def concave(x,y,color):
    global answer,answer_index
    if y<=14:
        for i in range(5):
            if arr[x][y+i]!=color:
                break
            if i+1==5:
                if y-1<0 or arr[x][y-1]!=color:
                    if y+5>18 or arr[x][y+5]!=color:
                        answer=color
                        answer_index=[x+1,y+1]
                        return
    if x<=14:
        for i in range(5):
            if arr[x+i][y]!=color:
                break
            if i+1==5:
                if x-1<0 or arr[x-1][y]!=color:
                    if x+5>18 or arr[x+5][y]!=color:
                        answer=color
                        answer_index=[x+1,y+1]
                        return
    if x<=14 and y<=14:
        for i in range(5):
            if arr[x+i][y+i]!=color:
                break
            if i+1==5:
                if x-1<0 or y-1<0 or arr[x-1][y-1]!=color:
                    if x+5>18 or y+5>18 or arr[x+5][y+5]!=color:
                        answer=color
                        answer_index=[x+1,y+1]
                        return
    if x<=14 and y>=4:
        for i in range(5):
            if arr[x+i][y-i]!=color:
                break
            if i+1==5:
                if x-1<0 or y+1>18 or arr[x-1][y+1]!=color:
                    if x+5>18 or y-5<0 or arr[x+5][y-5]!=color:
                        answer=color
                        answer_index=[x+5,y-3]
                        return
for i in range(19):
    for j in range(19):
        if answer!=0:
            break
        if arr[i][j]==1 or arr[i][j]==2:
            concave(i,j,arr[i][j])
    if answer!=0:
        break
print(answer)
if answer!=0:
    print(*answer_index)