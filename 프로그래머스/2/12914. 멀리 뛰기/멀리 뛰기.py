def solution(n):
    answer = 0
    fibo=[1,2]
    for i in range(n):
        fibo.append(fibo[-1]+fibo[-2])
    return fibo[n-1]%1234567