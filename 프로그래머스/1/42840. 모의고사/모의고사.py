def solution(answers):
    answer = []
    score=[0,0,0]
    person1=[1, 2, 3, 4, 5]
    person2=[2, 1, 2, 3, 2, 4, 2, 5]
    person3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if answers[i]==person1[i%len(person1)]:
            score[0]+=1
        if answers[i]==person2[i%len(person2)]:
            score[1]+=1
        if answers[i]==person3[i%len(person3)]:
            score[2]+=1
    maxscore=max(score)
    for i in range(len(score)):
        if score[i]==maxscore:
            answer.append(i+1)
    return answer