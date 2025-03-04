import sys
answer=[]
while(1):
    a,b=map(int,sys.stdin.readline().split())
    if a==0 and b==0:
        break
    elif a==b:
        print(a,b,2)
    else:
        ab=[a,b]
        a_circle=[a]
        while(1):
            now=0
            while(a>0):
                now+=(a%10)**2
                a//=10
            if now in a_circle:
                break
            else:
                a_circle.append(now)
                a=now
        b_circle=[b]
        while(1):
            now=0
            while(b>0):
                now+=(b%10)**2
                b//=10
            if now in b_circle:
                break
            else:
                b_circle.append(now)
                b=now
        small_num=[]
        for i in a_circle:
            if i in b_circle:
                small_num.append(a_circle.index(i)+b_circle.index(i)+2)
                break
        for i in b_circle:
            if i in a_circle:
                small_num.append(a_circle.index(i)+b_circle.index(i)+2)
                break
        if len(small_num)==0:
            print(ab[0],ab[1],0)
        else:
            print(ab[0],ab[1],min(small_num))