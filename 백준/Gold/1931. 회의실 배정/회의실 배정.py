num=int(input())
arr=[list(map(int,input().split())) for _ in range(num)]
arr.sort(key=lambda x:(x[1],x[0]))
answer=[arr[0]]
for i in range(1,num):
    if answer[len(answer)-1][1]<=arr[i][0]:
        answer.append(arr[i])
print(len(answer))