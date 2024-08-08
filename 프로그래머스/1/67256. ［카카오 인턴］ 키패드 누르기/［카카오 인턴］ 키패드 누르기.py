def solution(numbers, hand):
    answer = ''
    left='*'
    right='#'
    for i in numbers:
        print(left,right,i)
        if i==1 or i==4 or i==7:
            answer+='L'
            left=i
        elif i==3 or i==6 or i==9:
            answer+='R'
            right=i
        else:
            num=i
            if i==0:
                num=11
            newl=0
            newr=0
            if left==1 or left==4 or left==7:
                newl=abs(left+1-num)//3+1
            elif left=='*':
                newl=abs(11-num)//3+1
            else:
                if left==0:
                    newl=abs(11-num)//3
                else:
                    newl=abs(left-num)//3
            if right==3 or right==6 or right==9:
                newr=abs(right-1-num)//3+1
            elif right=='#':
                newr=abs(11-num)//3+1
            else:
                if right==0:
                    newr=abs(11-num)//3
                else:
                    newr=abs(right-num)//3
            if newl==newr:
                if hand=='left':
                    answer+='L'
                    left=i
                else:
                    answer+='R'
                    right=i
            elif newl<newr:
                answer+='L'
                left=i
            else:
                answer+='R'
                right=i
    return answer