def solution(numer1, denom1, numer2, denom2):
    answer = []
    common=1
    for i in range(1,min(denom1,denom2)+1):
        if denom1%i==0 and denom2%i==0:
            common=i
    commonnum=common*(denom1//common)*(denom2//common)
    answer.append(commonnum//denom1*numer1+commonnum//denom2*numer2)
    answer.append(commonnum)
    divide=1
    for i in range(1,min(answer[0],answer[1])+1):
        if answer[0]%i==0 and answer[1]%i==0:
            divide=i
    answer[0]//=divide
    answer[1]//=divide
    return answer