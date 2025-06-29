import sys
duck=list(sys.stdin.readline().strip())
duck_sound=['q','u','a','c','k']
answer=0
while(True):
    cnt=0
    arr=[]
    for i in range(len(duck)):
        if duck[i]==duck_sound[cnt%5]:
            arr.append(i)
            cnt+=1
            if len(arr)==5:
                for j in arr:
                    duck[j]=''
                arr=[]
    if cnt>=5:
        answer+=1
    else:
        break
if answer==0 or duck!=['']*len(duck):
    print(-1)
else:
    print(answer)