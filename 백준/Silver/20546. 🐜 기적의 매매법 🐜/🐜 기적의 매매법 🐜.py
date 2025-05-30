import sys
money=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
junhyun_money=money
junhyun_stock=0
sungmin_money=money
sungmin_stock=0
stock_increase=0
stock_decrease=0
for i in range(14):
    if junhyun_money//arr[i]>0:
        junhyun_stock+=(junhyun_money//arr[i])
        junhyun_money-=(junhyun_money//arr[i]*arr[i])
    if i==0 or arr[i]==arr[i-1]:
        continue
    elif arr[i]==arr[i-1]:
        stock_increase=0
        stock_decrease=0
    elif arr[i]>arr[i-1]:
        if stock_decrease!=0:
            stock_increase=1
            stock_decrease=0
        else:
            stock_increase+=1
    elif arr[i]<arr[i-1]:
        if stock_increase!=0:
            stock_increase=0
            stock_decrease=1
        else:
            stock_decrease+=1
    if stock_increase>=3:
        sungmin_money+=(sungmin_stock*arr[i])
        sungmin_stock=0
    elif stock_decrease>=3:
        sungmin_stock+=(sungmin_money//arr[i])
        sungmin_money-=(sungmin_money//arr[i]*arr[i])
junhyun=junhyun_money+junhyun_stock*arr[13]
sungmin=sungmin_money+sungmin_stock*arr[13]
if junhyun>sungmin:
    print("BNP")
elif junhyun==sungmin:
    print("SAMESAME")
else:
    print("TIMING")