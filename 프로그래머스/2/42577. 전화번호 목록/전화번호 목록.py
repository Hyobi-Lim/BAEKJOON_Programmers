def solution(phone_book):
    answer = True
    numset=set()
    for i in phone_book:
        numset.add(len(i))
    for i in numset:
        real=set()
        now=set()
        for j in phone_book:
            if len(j)==i:
                real.add(j)
            else:
                now.add(j[:i])
        for j in real:
            if j in now:
                answer=False
                break
    return answer