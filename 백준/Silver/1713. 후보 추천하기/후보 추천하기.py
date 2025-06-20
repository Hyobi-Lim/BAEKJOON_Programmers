import sys
n=int(sys.stdin.readline())
length=int(sys.stdin.readline())
student=list(map(int,sys.stdin.readline().split()))
answer_dict=dict()
for i in student:
    if len(answer_dict)<n:
        answer_dict[i]=answer_dict.get(i,0)+1
    else:
        if i in answer_dict:
            answer_dict[i]+=1
        else:
            min_student=''
            min_recommendation=2000
            for j in answer_dict:
                if min_recommendation>answer_dict[j]:
                    min_recommendation=answer_dict[j]
                    min_student=j
            del answer_dict[min_student]
            answer_dict[i]=1
answer_keys=list(answer_dict.keys())
answer_keys.sort()
print(*answer_keys)