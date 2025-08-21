import math
def solution(arrayA, arrayB):
    answer = 0
    arrayA.sort()
    arrayB.sort()
    divisor_a_li=[]
    divisor_b_li=[]
    divisor_a=0
    divisor_b=0
    for i in range(int(math.sqrt(arrayA[0])),0,-1):
        if(arrayA[0]%i==0):
            for j in arrayA:
                if(j%(arrayA[0]//i)!=0):
                    break
                else:
                    if(j==arrayA[-1]):
                        divisor_a_li.append(arrayA[0]//i)
            for j in arrayA:
                if(j%i!=0):
                    break
                else:
                    if(j==arrayA[-1]):
                        divisor_a_li.append(i)
    for i in range(int(math.sqrt(arrayB[0])),0,-1):
        if(arrayB[0]%i==0):
            for j in arrayB:
                if(j%(arrayB[0]//i)!=0):
                    break
                else:
                    if(j==arrayB[-1]):
                        divisor_b_li.append(arrayB[0]//i)
            for j in arrayB:
                if(j%i!=0):
                    break
                else:
                    if(j==arrayB[-1]):
                        divisor_b_li.append(i)
    if(len(divisor_a_li)!=0):
        divisor_a=max(divisor_a_li)
    if(len(divisor_b_li)!=0):
        divisor_b=max(divisor_b_li)
    if(divisor_a==0 and divisor_b==0):
        return 0
    elif(divisor_a==0):
        for i in range(divisor_b,1,-1):
            if(divisor_b%i==0):
                for j in arrayA:
                    if(j%i==0):
                        break
                    else:
                        if(j==arrayA[-1]):
                            answer=i
                if(answer!=0):
                    break
    elif(divisor_b==0):
        for i in range(divisor_a,1,-1):
            if(divisor_a%i==0):
                for j in arrayB:
                    if(j%i==0):
                        break
                    else:
                        if(j==arrayB[-1]):
                            answer=i
                if(answer!=0):
                    break
    else:
        for i in range(divisor_b,1,-1):
            if(divisor_b%i==0):
                for j in arrayA:
                    if(j%i==0):
                        break
                    else:
                        if(j==arrayA[-1]):
                            answer=i
                if(answer!=0):
                    break
        change=False
        for i in range(divisor_a,1,-1):
            if(divisor_a%i==0):
                for j in arrayB:
                    if(j%i==0):
                        break
                    else:
                        if(j==arrayB[-1] and answer<i):
                            answer=i
                            change=True
                if(change):
                    break
    return answer