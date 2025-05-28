import sys
a=int(sys.stdin.readline())
t=int(sys.stdin.readline())
zero_one=int(sys.stdin.readline())
zero_one_num=[0,0]
cnt=2
answer=-1
done=False
while(True):
    zero_one_num[0]+=1
    answer+=1
    if (zero_one==0 and zero_one_num[0]==t) or (zero_one==1 and zero_one_num[1]==t):
        break
    zero_one_num[1]+=1
    answer+=1
    if (zero_one==0 and zero_one_num[0]==t) or (zero_one==1 and zero_one_num[1]==t):
        break
    zero_one_num[0]+=1
    answer+=1
    if (zero_one==0 and zero_one_num[0]==t) or (zero_one==1 and zero_one_num[1]==t):
        break
    zero_one_num[1]+=1
    answer+=1
    if (zero_one==0 and zero_one_num[0]==t) or (zero_one==1 and zero_one_num[1]==t):
        break
    for i in range(2):
        for j in range(cnt):
            zero_one_num[i]+=1
            answer+=1
            if (zero_one==0 and zero_one_num[0]==t) or (zero_one==1 and zero_one_num[1]==t):
                done=True
                break
        if done==True:
            break
    cnt+=1
    if done==True:
        break
print(answer%a)