import sys
n=int(sys.stdin.readline())
guest=[]
for i in range(n):
    arr=list(sys.stdin.readline().split())
    for j in range(5):
        arr[j]=arr[j].split('-')
        arr[j][1]=int(arr[j][1])
    guest+=arr
guest=guest[::-1]
sortguest=sorted(guest,key=lambda x:(x[0],x[1]))
waiting=[]
finalguest=[]
while(1):
    if len(sortguest)==len(finalguest):
        break
    if sortguest[len(finalguest)] in guest:
        while(sortguest[len(finalguest)] in guest):
            now=guest.pop()
            if now==sortguest[len(finalguest)]:
                finalguest.append(now)
                break
            else:
                waiting.append(now)
    elif sortguest[len(finalguest)] in waiting:
        if sortguest[len(finalguest)]==waiting[len(waiting)-1]:
            finalguest.append(waiting.pop())
        else:
            break
    else:
        break
if sortguest==finalguest:
    print("GOOD")
else:
    print("BAD")