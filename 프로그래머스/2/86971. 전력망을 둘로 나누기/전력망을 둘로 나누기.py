from copy import deepcopy
def solution(n, wires):
    answer = -1
    all=[[0] * (n+1) for _ in range(n+1)]
    for i in wires:
        all[i[0]][i[1]]=1
        all[i[1]][i[0]]=1
    for i in wires:
        now=deepcopy(all)
        now[i[0]][i[1]]=0
        now[i[1]][i[0]]=0
        stack=[i[0]]
        visited=[]
        while stack:
            nowhere=stack.pop()
            if nowhere not in visited:
                visited.append(nowhere)
            for j in range(n+1):
                if j not in visited and now[nowhere][j]:
                    stack.append(j)
        if answer==-1 or abs(n-len(visited)*2)<answer:
            answer=abs(n-len(visited)*2)
    return answer