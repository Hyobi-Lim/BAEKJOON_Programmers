def solution(n):
    answer = 0
    num1=n
    num2=0
    for i in range(n//2+1):
        num=1
        for j in range(min(num1,num2)):
            num*=(num1+num2-j)
        for k in range(min(num1,num2)):
            num//=(k+1)
        answer+=num
        num1-=2
        num2+=1
    answer%=1234567
    return answer