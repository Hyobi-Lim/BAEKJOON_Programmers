answer = 0
def perm(depth,check,arr,sel,k):
    global answer
    if depth == len(arr):
        num=k
        count=0
        for i in sel:
            if num>=i[0]:
                num-=i[1]
                count+=1
            else:
                break
        if count>answer:
            answer=count
        return

    for i in range(len(arr)):
        if not check[i]:
            check[i] = 1
            sel[depth] = arr[i]
            perm(depth+1,check,arr,sel,k)
            check[i] = 0

def solution(k, dungeons):
    sel = [0]*len(dungeons)
    check = [0]*len(dungeons)
    perm(0,check,dungeons,sel,k)
    return answer