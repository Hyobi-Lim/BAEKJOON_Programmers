import sys
from collections import deque
n=int(sys.stdin.readline())
left=['.']*n
right=['.']*n
ancestors=['.']*n
for i in range(n):
    a,b,c=sys.stdin.readline().split()
    left[ord(a)-ord('A')]=b
    right[ord(a)-ord('A')]=c
    if b!='.':
        ancestors[ord(b)-ord('A')]=a
    if c!='.':
        ancestors[ord(c)-ord('A')]=a
root=0
def preorder(node):
    if node>=0:
        print(chr(ord('A')+node),end='')
        preorder(ord(left[node])-ord('A'))
        preorder(ord(right[node])-ord('A'))
def inorder(node):
    if node>=0:
        inorder(ord(left[node])-ord('A'))
        print(chr(ord('A')+node),end='')
        inorder(ord(right[node])-ord('A'))
def postorder(node):
    if node>=0:
        postorder(ord(left[node])-ord('A'))
        postorder(ord(right[node])-ord('A'))
        print(chr(ord('A')+node),end='')
preorder(root)
print()
inorder(root)
print()
postorder(root)