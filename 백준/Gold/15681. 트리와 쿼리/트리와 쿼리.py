import sys
sys.setrecursionlimit(10**6)
N,R,Q=map(int,sys.stdin.readline().split(' '))
Varr=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b=map(int,sys.stdin.readline().split(' '))
    Varr[a].append(b)
    Varr[b].append(a)
U=[int(input()) for _ in range(Q)]
parentNode=dict()
childNode=dict()
def makeTree(currentNode,parent):
    parentNode[currentNode]=parent
    for i in Varr[currentNode]:
        if i!=parent:
            if currentNode not in childNode:
                childNode[currentNode]=[i]
            else:
                childNode[currentNode].append(i)
            makeTree(i,currentNode)
makeTree(R,-1)
size=dict()
def countSubtreeNode(currentNode):
    size[currentNode]=1
    if currentNode in childNode:
        for i in childNode[currentNode]:
            countSubtreeNode(i)
            size[currentNode]+=size[i]
countSubtreeNode(R)
for i in U:
    print(size[i])