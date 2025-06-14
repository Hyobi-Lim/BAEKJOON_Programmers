import sys
n,m=map(int,sys.stdin.readline().split())
friends=dict()
for i in range(m):
    a,b=map(int,sys.stdin.readline().split())
    if a not in friends:
        friends[a]=[b]
    else:
        friends[a].append(b)
    if b not in friends:
        friends[b]=[a]
    else:
        friends[b].append(a)
answer=0
def friends_check(friends_set,now):
    global answer
    if answer==1:
        return
    if len(friends_set)==5:
        answer=1
        return
    else:
        for i in friends[now]:
            if i not in friends_set:
                friends_check(friends_set|set([i]),i)
for i in range(n):
    if i in friends and answer!=1:
        friends_check(set([i]),i)
print(answer)