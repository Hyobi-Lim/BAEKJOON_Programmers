def solution(wallpaper):
    answer = [len(wallpaper),len(wallpaper[0]),0,0]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j]=='#':
                if answer[0]>i:
                    answer[0]=i
                if answer[1]>j:
                    answer[1]=j
                if answer[2]<i+1:
                    answer[2]=i+1
                if answer[3]<j+1:
                    answer[3]=j+1
    return answer