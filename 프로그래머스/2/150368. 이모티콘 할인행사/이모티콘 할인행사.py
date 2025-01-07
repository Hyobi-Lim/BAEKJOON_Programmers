def solution(users, emoticons):
    answer = [0,0]
    def discount(discountrate,price,now,num,users):
        nonlocal answer
        if now==num:
            nowemo=[0,0]
            for i in users:
                nowbuy=0
                for j in range(len(price)):
                    if discountrate[j]>=i[0]:
                        nowbuy+=price[j]*(1-discountrate[j]/100)
                if nowbuy<i[1]:
                    nowemo[1]+=nowbuy
                else:
                    nowemo[0]+=1
            if nowemo[0]>answer[0]:
                answer=nowemo
            elif nowemo[0]==answer[0] and nowemo[1]>answer[1]:
                answer=nowemo
            return
        else:
            for i in range(10,50,10):
                newdiscountrate=discountrate[:]
                newdiscountrate[now-1]=i
                discount(newdiscountrate,price,now+1,num,users)
    discount([0]*len(emoticons),emoticons,0,len(emoticons),users)
    return answer