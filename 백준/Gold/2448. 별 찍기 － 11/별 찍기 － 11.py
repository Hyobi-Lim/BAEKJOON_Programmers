import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    now=' '*(n-i-1)+'*'*i+'*'+'*'*i+' '*(n-i-1)
    arr.append(list(now))
def triangle(num,now_x,now_y):
    if num==3:
        arr[now_x-2][now_y-1]=' '
        return
    else:
        for i in range(num//2):
            for j in range(i*2+1):
                arr[now_x-1-i][now_y-1-i+j]=' '
        triangle(num//2,now_x-num//2,now_y)
        triangle(num//2,now_x,now_y-num//2)
        triangle(num//2,now_x,now_y+num//2)
triangle(n,n,n)
for i in range(n):
    print(''.join(arr[i]))