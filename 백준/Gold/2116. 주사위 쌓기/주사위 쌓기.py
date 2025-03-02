import sys
n=int(sys.stdin.readline())
dice=dict()
dice_sum=[]
for i in range(n):
    arr=list(map(int,sys.stdin.readline().split()))
    dice[i]=dict()
    for j in range(3):
        if j==0:
            dice[i][arr[j]]=arr[5]
            dice[i][arr[5]]=arr[j]
        else:
            dice[i][arr[j]]=arr[j+2]
            dice[i][arr[j+2]]=arr[j]
for i in range(1,7):
    num=dice[0][i]
    dicenum=[1,2,3,4,5,6]
    dicenum.remove(num)
    dicenum.remove(dice[0][num])
    nowsum=max(dicenum)
    for j in range(1,n):
        num=dice[j][num]
        dicenum=[1,2,3,4,5,6]
        dicenum.remove(num)
        dicenum.remove(dice[j][num])
        nowsum+=max(dicenum)
    dice_sum.append(nowsum)
print(max(dice_sum))