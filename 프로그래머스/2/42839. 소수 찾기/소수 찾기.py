all=[]
sel = [0]
check = [0]
def perm(depth,numbers,num):
    global all
    if check.count(1) == num:
        all.append(sel[:])
        return

    for i in range(len(numbers)):
        if not check[i]:
            check[i] = 1
            sel[depth] = numbers[i]
            perm(depth+1,numbers,num)
            check[i] = 0
    
def solution(numbers):
    global sel,check
    answer = 0
    numbers=list(numbers)
    check = [0]*len(numbers)
    for i in range(1,len(numbers)+1):
        sel = [0]*i
        perm(0,numbers,i)
    for i in range(len(all)):
        all[i]=int(''.join(all[i]))
    nosameall=set(all)
    for i in nosameall:
        num=0
        for j in range(1,i+1):
            if i%j==0:
                num+=1
            if num>=3:
                break
        if num==2:
            answer+=1
    return answer