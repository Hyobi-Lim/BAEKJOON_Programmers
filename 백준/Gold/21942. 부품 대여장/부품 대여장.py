import sys
n,l,f=sys.stdin.readline().split()
n=int(n)
l=1440*int(l[:3])+60*int(l[4:6])+int(l[7:])
f=int(f)
month={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
rental=dict()
price=dict()
for i in range(n):
    date,time,item,name=sys.stdin.readline().split()
    now_month=int(date[5:7])
    now_day=int(date[8:])
    now_hour=int(time[:2])
    now_minute=int(time[3:])
    if (item,name) not in rental:
        rental[(item,name)]=[now_month,now_day,now_hour,now_minute]
    else:
        prev_month,prev_day,prev_hour,prev_minute=rental[(item,name)]
        d=month[prev_month]-prev_day+now_day
        if prev_month==now_month:
            d=now_day-prev_day
        else:
            for j in range(prev_month+1,now_month):
                d+=month[j]
        m=0
        if now_hour<prev_hour or (now_hour==prev_hour and now_minute<prev_minute):
            d-=1
            m+=(60-prev_minute+now_minute)
            m+=(60*(23-prev_hour+now_hour))
        else:
            m+=(60*now_hour+now_minute)
            m-=(60*prev_hour+prev_minute)
        all_minute=1440*d+m
        if all_minute>l:
            if name not in price:
                price[name]=(all_minute-l)*f
            else:
                price[name]+=(all_minute-l)*f
        del rental[(item,name)]
if len(price)==0:
    print(-1)
else:
    price_keys=list(price.keys())
    price_keys.sort()
    for i in price_keys:
        print(i,price[i])