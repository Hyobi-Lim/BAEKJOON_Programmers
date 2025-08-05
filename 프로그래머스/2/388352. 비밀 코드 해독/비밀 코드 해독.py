def solution(n, q, ans):
    answer = 0
    for a in range(1,n-3):
        for b in range(a+1,n-2):
            for c in range(b+1,n-1):
                for d in range(c+1,n):
                    for e in range(d+1,n+1):
                        for i in range(len(q)):
                            num=0
                            if a in q[i]:
                                num+=1
                            if b in q[i]:
                                num+=1
                            if c in q[i]:
                                num+=1
                            if d in q[i]:
                                num+=1
                            if e in q[i]:
                                num+=1
                            if num!=ans[i]:
                                break
                            if i==len(q)-1:
                                answer+=1
    return answer