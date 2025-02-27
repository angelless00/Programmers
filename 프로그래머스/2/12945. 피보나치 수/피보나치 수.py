def solution(n):
    answer = 0
    fibo=[0,1]
    for i in range(n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo[n]%1234567