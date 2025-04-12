import sys
n=int(sys.stdin.readline())
for i in range(n):
    num=int(sys.stdin.readline())
    if num%10==0:
        num//=10
    else:
        num//=10
        num+=1
    numbers=[]
    for j in range(num):
        numbers+=list(map(int,sys.stdin.readline().split()))
    now=[numbers[0]]
    answer=[numbers[0]]
    for j in range(len(numbers)//2):
        now+=numbers[2*j+1:2*(j+1)+1]
        now.sort()
        answer.append(now[len(now)//2])
    print(len(answer))
    num=len(answer)
    if num%10==0:
        num//=10
    else:
        num//=10
        num+=1
    for j in range(num):
        if j<num-1:
            print(*answer[10*j:10*(j+1)])
        else:
            print(*answer[10*j:])