all=[]
def perm(arr,sen):
    global all
    if len(sen) == 5:
        return
    for i in arr:
        sen+=i
        all.append(sen)
        perm(arr,sen)
        sen=sen[:len(sen)-1]

def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    sen=''
    perm(arr,'')
    all.sort()
    answer = all.index(word)+1
    return answer