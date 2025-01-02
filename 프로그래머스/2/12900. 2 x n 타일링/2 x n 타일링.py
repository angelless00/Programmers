def solution(n):
    answer=1
    a_0=0
    
    # 피보나치수열
    for i in range(n):
        a_0,answer=answer,a_0+answer
    return answer%1000000007