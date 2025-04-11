import sys
tree_dict=dict()
tree_name=set()
tree_num=0
while True:
    tree=sys.stdin.readline().rstrip()
    if not tree:
        break
    if tree not in tree_dict:
        tree_dict[tree]=1
    else:
        tree_dict[tree]+=1
    tree_name.add(tree)
    tree_num+=1
tree_name=list(tree_name)
tree_name.sort()
for i in tree_name:
    print(i,"%.4f"%(tree_dict[i]/tree_num*100))