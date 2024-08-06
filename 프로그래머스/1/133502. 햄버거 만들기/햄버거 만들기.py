def solution(ingredient):
    answer = 0
    hamburger=''
    for i in ingredient:
        hamburger+=str(i)
        if hamburger[len(hamburger)-4:]=='1231':
            answer+=1
            hamburger=hamburger[:len(hamburger)-4]
    return answer