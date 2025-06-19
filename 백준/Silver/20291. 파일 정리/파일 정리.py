import sys
n=int(sys.stdin.readline())
file_dict=dict()
for i in range(n):
    file=sys.stdin.readline().strip().split('.')
    file_dict[file[1]]=file_dict.get(file[1],0)+1
file_keys=list(file_dict.keys())
file_keys.sort()
for i in file_keys:
    print(i,file_dict[i])