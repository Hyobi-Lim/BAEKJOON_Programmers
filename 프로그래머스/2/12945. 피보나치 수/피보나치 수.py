def solution(n):
    fibonacci=[0,1]
    while(len(fibonacci)!=n+1):
        fibonacci.append((fibonacci[len(fibonacci)-1]+fibonacci[len(fibonacci)-2])%1234567)
    return fibonacci[len(fibonacci)-1]