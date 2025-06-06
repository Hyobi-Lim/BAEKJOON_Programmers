import sys
left_hand={'q':[0,0],'w':[0,1],'e':[0,2],'r':[0,3],'t':[0,4],
           'a':[1,0],'s':[1,1],'d':[1,2],'f':[1,3],'g':[1,4],
           'z':[2,0],'x':[2,1],'c':[2,2],'v':[2,3]}
right_hand={'y':[0,5],'u':[0,6],'i':[0,7],'o':[0,8],'p':[0,9],
           'h':[1,5],'j':[1,6],'k':[1,7],'l':[1,8],
           'b':[2,4],'n':[2,5],'m':[2,6]}
left,right=list(sys.stdin.readline().split())
sentence=list(sys.stdin.readline().strip())
answer=len(sentence)
for i in sentence:
    if i in left_hand:
        answer+=(abs(left_hand[i][1]-left_hand[left][1])+abs(left_hand[i][0]-left_hand[left][0]))
        left=i
    else:
        answer+=(abs(right_hand[i][1]-right_hand[right][1])+abs(right_hand[i][0]-right_hand[right][0]))
        right=i
print(answer)