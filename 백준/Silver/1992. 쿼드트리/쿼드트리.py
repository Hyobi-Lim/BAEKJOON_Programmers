import sys
n=int(sys.stdin.readline())
arr=[]
for i in range(n):
    arr.append(list(sys.stdin.readline().strip()))
answer=''
def quad_tree(num,start_x,start_y):
    global answer
    if num==1:
        answer+=arr[start_x][start_y]
        return
    else:
        now=[]
        for i in range(num):
            now+=arr[start_x+i][start_y:start_y+num]
        if '0' in now and '1' in now:
            new_num=num//2
            answer+='('
            quad_tree(new_num,start_x,start_y)
            quad_tree(new_num,start_x,start_y+new_num)
            quad_tree(new_num,start_x+new_num,start_y)
            quad_tree(new_num,start_x+new_num,start_y+new_num)
            answer+=')'
        elif '0' in now:
            answer+='0'
        else:
            answer+='1'
quad_tree(n,0,0)
print(answer)