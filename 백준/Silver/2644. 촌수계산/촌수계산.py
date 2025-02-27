import sys
answer=-1
def find_route(all_pc,end,route,num):   
    global answer
    if route[len(route)-1]==end:
        answer=len(route)-1
        return
    else:
        for i in all_pc[route[len(route)-1]]:
            if i not in route:
                newroute=route[:]
                newroute.append(i)
                find_route(all_pc,end,newroute,num+1)
n=int(sys.stdin.readline())
start,end=map(int,sys.stdin.readline().split())
num=int(sys.stdin.readline())
pc=dict()
for i in range(num):
    parent,child=map(int,sys.stdin.readline().split())
    if parent not in pc:
        pc[parent]=[child]
    else:
        pc[parent].append(child)
    if child not in pc:
        pc[child]=[parent]
    else:
        pc[child].append(parent)
find_route(pc,end,[start],0)
print(answer)