import sys
answer=-1
xy=[
    [[0,0],[0,1],[0,2]],
    [[1,0],[1,1],[1,2]],
    [[2,0],[2,1],[2,2]],
    [[0,0],[1,0],[2,0]],
    [[0,1],[1,1],[2,1]],
    [[0,2],[1,2],[2,2]],
    [[0,0],[1,1],[2,2]],
    [[0,2],[1,1],[2,0]]
   ]
def check(arr,index,cnt,visited):
    global answer
    if index>=8:
        all_arr=[]
        for i in arr:
            all_arr+=i
        if 'H' not in all_arr or 'T' not in all_arr:
            if answer==-1 or answer>cnt:
                answer=cnt
        return
    all_arr=[]
    for i in arr:
        all_arr+=i
    if 'H' not in all_arr or 'T' not in all_arr:
        if answer==-1 or answer>cnt:
            answer=cnt
    else:
        check(arr,index+1,cnt,visited)
        for x,y in xy[index]: 
            if arr[x][y]=='H':
                arr[x][y]='T'
            else:
                arr[x][y]='H'
        check(arr,index+1,cnt+1,visited+[index])
        for x,y in xy[index]:
            if arr[x][y]=='H':
                arr[x][y]='T'
            else:
                arr[x][y]='H'
t=int(sys.stdin.readline())
for i in range(t):
    answer=-1
    arr=[list(sys.stdin.readline().split()) for _ in range(3)]
    check(arr,0,0,[])
    print(answer)