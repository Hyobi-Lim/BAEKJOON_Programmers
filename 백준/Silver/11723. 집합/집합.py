import sys
m=int(sys.stdin.readline())
s=set()
for i in range(m):
    cal=sys.stdin.readline().split()
    if cal[0]=='all':
        s=set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    elif cal[0]=='empty':
        s=set()
    elif cal[0]=='add':
        s.add(int(cal[1]))
    elif cal[0]=='remove':
        s.discard(int(cal[1]))
    elif cal[0]=='check':
        if int(cal[1]) in s:
            print(1)
        else:
            print(0)
    else:
        if int(cal[1]) in s:
            s.remove(int(cal[1]))
        else:
            s.add(int(cal[1]))