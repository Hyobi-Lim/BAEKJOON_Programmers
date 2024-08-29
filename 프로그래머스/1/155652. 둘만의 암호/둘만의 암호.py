def solution(s, skip, index):
    answer = ''
    skiplist=[]
    for i in s:
        now=i
        while(len(skiplist)!=index):
            now=chr(ord(now)+1)
            if ord(now)>ord('z'):
                now=chr(ord(now)-26)
            if now not in skip:
                skiplist.append(now)
        answer+=skiplist[len(skiplist)-1]
        skiplist=[]
    return answer