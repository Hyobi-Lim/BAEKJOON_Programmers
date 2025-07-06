import sys
n,m,r=map(int,sys.stdin.readline().split())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
for i in range(min(n,m)//2):
    num=2*(n+m)-4*(2*i+1)
    move_num=r%num
    all_idx=[]
    for k in range(i,m-i-1):
        all_idx.append([i,k])
        #print(i,k)
    for k in range(i,n-i-1):
        all_idx.append([k,m-i-1])
        #print(k,m-i-1)        
    for k in range(m-i-1,i,-1):
        all_idx.append([n-i-1,k])
        #print(n-i-1,k)
    for k in range(n-i-1,i,-1):
        all_idx.append([k,i])
        #print(k,i)
    temp=[]
    for j in range(len(all_idx)):
        from_x,from_y=all_idx[j]
        to_x,to_y=all_idx[j-move_num]
        if j<move_num:
            temp.append(arr[to_x][to_y])
        if j>=len(all_idx)-move_num:
            arr[to_x][to_y]=temp[j-len(all_idx)+move_num]
        else:
            arr[to_x][to_y]=arr[from_x][from_y]
for i in arr:
    print(*i)