def solution(numbers):
    answer = [0]*(len(numbers)-1)
    largest=max(numbers[1:])
    li=[]
    rev=numbers[:]
    rev.sort(reverse=True)
    if rev==numbers:
        answer = [-1]*(len(numbers))
    else:
        for i in range(len(numbers)):
            if i==len(numbers)-1:
                for j in li:
                    answer[j]=numbers[len(numbers)-1]
                answer.append(-1)
            elif numbers[i]>=largest:
                answer[i]=-1
                for j in li:
                    answer[j]=numbers[i]
                li=[]
                largest=max(numbers[i+1:])
            else:
                if len(li)==0:
                    li.append(i)
                elif numbers[i]<=numbers[li[len(li)-1]]:
                    li.append(i)
                else:
                    while(1):
                        if len(li)!=0 and numbers[i]>numbers[li[len(li)-1]]:
                            answer[li[len(li)-1]]=numbers[i]
                            li.pop()
                        else:
                            break
                    li.append(i)
    return answer