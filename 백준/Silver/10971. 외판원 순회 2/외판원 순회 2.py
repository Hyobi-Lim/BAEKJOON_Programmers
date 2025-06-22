import sys
n=int(sys.stdin.readline())
arr=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
answer=0
def circuit(cnt,visited):
    global answer
    start=visited[0]
    end=visited[-1]
    if answer!=0 and answer<=cnt:
        return
    if len(visited)==n:
        if arr[end][start]!=0:
            cnt+=arr[end][start]
            if answer==0 or answer>cnt:
                answer=cnt
        return
    for i in range(n):
        if i not in visited:
            if arr[end][i]!=0:
                circuit(cnt+arr[end][i],visited+[i])
for i in range(n):
    circuit(0,[i])
print(answer)