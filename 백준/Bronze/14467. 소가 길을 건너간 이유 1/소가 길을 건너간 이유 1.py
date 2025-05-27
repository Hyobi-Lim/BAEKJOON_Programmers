import sys
n=int(sys.stdin.readline())
cow=dict()
answer=0
for i in range(n):
    cow_num,location=map(int,sys.stdin.readline().split())
    if cow_num not in cow:
        cow[cow_num]=location
    else:
        if cow[cow_num]==location:
            continue
        else:
            answer+=1
            cow[cow_num]=location
print(answer)