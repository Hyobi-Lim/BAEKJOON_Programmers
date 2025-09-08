def solution(numbers):
    answer = ''
    max_len=0
    for i in range(len(numbers)):
        numbers[i]=str(numbers[i])
        if max_len<len(numbers[i]):
            max_len=len(numbers[i])
    numbers_dict=dict()
    for i in numbers:
        word=i*4
        word=word[:4]
        if word in numbers_dict:
            numbers_dict[word].append(i)
        else:
            numbers_dict[word]=[i]
    for i in numbers_dict:
        numbers_dict[i].sort(reverse=True)
    numbers_dict_key=list(numbers_dict.keys())
    numbers_dict_key.sort(reverse=True)
    for i in numbers_dict_key:
        for j in numbers_dict[i]:
            answer+=j
    if int(answer)==0:
        answer="0"
    return answer