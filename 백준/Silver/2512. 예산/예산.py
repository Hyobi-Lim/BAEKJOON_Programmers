import sys
n=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
maximum=int(sys.stdin.readline())
if maximum>=sum(arr):
    print(max(arr))
else:
    arr.sort()
    answer=maximum//len(arr)
    for i in range(len(arr)-1):
        if arr[i]<=(maximum-sum(arr[:i+1]))//(len(arr)-i-1):
            if answer<max(arr[i],(maximum-sum(arr[:i+1]))//(len(arr)-i-1)):
                answer=max(arr[i],(maximum-sum(arr[:i+1]))//(len(arr)-i-1))
    print(answer)