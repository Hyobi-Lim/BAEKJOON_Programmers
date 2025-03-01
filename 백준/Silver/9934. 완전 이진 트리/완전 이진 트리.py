import sys
k=int(sys.stdin.readline())
li=list(map(int,sys.stdin.readline().split()))
num=0
def inorder(tree,k):
    global num
    def _inorder(i = 0):
        global num
        if i >= len(tree):
            return
        _inorder(2 * i + 1)
        res[i]=li[num]
        num+=1
        _inorder(2 * i + 2)

    res = [0 for _ in range(2**k-1)]    
    _inorder()
    return res
inorder_li=inorder(li,k)
for i in range(k):
    for j in range(2**i-1,2**(i+1)-1):
        print(inorder_li[j],end=' ')
    print()