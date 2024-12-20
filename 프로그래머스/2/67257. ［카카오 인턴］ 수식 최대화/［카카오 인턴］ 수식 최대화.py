import re
def solution(expression):
    def calculate(calculateoperator,num1,num2):
        if calculateoperator=='+':
            return int(num1)+int(num2)
        elif calculateoperator=='-':
            return int(num1)-int(num2)
        else:
            return int(num1)*int(num2)
    answer = 0
    operator=['+','-','*']
    expression=re.split(r"(\+|\-|\*)",expression)
    for i in range(3):
        nowoperator=[operator[i]]
        for j in range(3):
            if operator[j] not in nowoperator:
                now2operator=nowoperator+[operator[j]]
                for k in range(3):
                    if operator[k] not in now2operator:
                        now3operator=now2operator+[operator[k]]
                        stack=[]
                        num=0
                        while num<len(expression):
                            if expression[num]==now3operator[0]:
                                stack[-1]=calculate(now3operator[0],stack[-1],expression[num+1])
                                num+=1
                            else:
                                stack.append(expression[num])
                            num+=1
                        stack2=[]
                        num=0
                        while num<len(stack):
                            if stack[num]==now3operator[1]:
                                stack2[-1]=calculate(now3operator[1],stack2[-1],stack[num+1])
                                num+=1
                            else:
                                stack2.append(stack[num])
                            num+=1
                        result=stack2[0]
                        for a in range(1,len(stack2),2):
                            result=calculate(now3operator[2],result,stack2[a+1])
                        if answer<abs(result):
                            answer=abs(result)
    return answer