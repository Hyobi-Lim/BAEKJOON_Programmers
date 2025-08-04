def solution(plans):
    answer = []
    for i in range(len(plans)):
        plans[i][1]=plans[i][1].split(":");
        plans[i][1]=int(plans[i][1][0])*60+int(plans[i][1][1])
        plans[i][2]=int(plans[i][2])
    plans.sort(key=lambda x:x[1])
    stack=[]
    for i in range(len(plans)):
        if i<len(plans)-1:
            if plans[i][1]+plans[i][2]<=plans[i+1][1]:
                answer.append(plans[i][0])
                time=plans[i+1][1]-(plans[i][1]+plans[i][2])
                while(len(stack)!=0 and time>0):
                    if time>=stack[-1][2]:
                        time-=stack[-1][2]
                        answer.append(stack[-1][0])
                        stack.pop()
                    else:
                        stack[-1][2]-=time
                        time=0
            else:
                plans[i][2]-=(plans[i+1][1]-plans[i][1])
                stack.append(plans[i])
        else:
            answer.append(plans[i][0])
            while(len(stack)!=0):
                answer.append(stack.pop()[0])
    return answer