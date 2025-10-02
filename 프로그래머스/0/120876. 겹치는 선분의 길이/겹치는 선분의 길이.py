def solution(lines):
    aline=[]
    bline=[]
    cline=[]
    all=set()
    for i in range(lines[0][0],lines[0][1]):
        aline.append(i)
    for i in range(lines[1][0],lines[1][1]):
        bline.append(i)
    for i in range(lines[2][0],lines[2][1]):
        cline.append(i)
    for i in aline:
        if i in bline or i in cline:
            all.add(i)
    for i in bline:
        if i in aline or i in cline:
            all.add(i)
    for i in cline:
        if i in aline or i in bline:
            all.add(i)
    return len(all)