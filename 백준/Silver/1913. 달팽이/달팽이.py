import sys
n=int(sys.stdin.readline())
target=int(sys.stdin.readline())
arr=[[0]*n for _ in range(n)]
num=1
x=n//2
y=n//2
target_xy=[0,0]
def check(x,y,target_num):
    global target_xy
    if arr[x][y]==target_num:
        target_xy=[x+1,y+1]
for i in range(n//2+1):
    if i==0:
        arr[x][y]=num
        check(x,y,target)
        num+=1
        x-=1
    else:
        for j in range(4):
            for k in range(2*i):
                if j==0:
                    arr[x][y]=num
                    check(x,y,target)
                    num+=1
                    y+=1
                elif j==1:
                    arr[x][y]=num
                    check(x,y,target)
                    num+=1
                    x+=1
                elif j==2:
                    arr[x][y]=num
                    check(x,y,target)
                    num+=1
                    y-=1
                else:
                    arr[x][y]=num
                    check(x,y,target)
                    num+=1
                    x-=1
            if j==0:
                y-=1
                x+=1
            elif j==1:
                x-=1
                y-=1
            elif j==2:
                y+=1
                x-=1
for i in arr:
    print(*i)
print(*target_xy)