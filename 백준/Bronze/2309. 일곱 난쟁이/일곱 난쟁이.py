import sys
arr=[]
for i in range(9):
    n=int(sys.stdin.readline())
    arr.append(n)
all=sum(arr)
for i in range(9):
    for j in range(i+1,9):
        if all-arr[i]-arr[j]==100:
            arr.remove(arr[j])
            arr.remove(arr[i])
            break
    if len(arr)!=9:
        break
arr.sort()
for i in range(7):
    print(arr[i])