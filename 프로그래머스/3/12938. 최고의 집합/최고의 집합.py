def solution(n, s):
    answer = []
    num=s//n
    remain=s%n
    if num ==0:
        answer=[-1]
    else:
        answer=[num for _ in range(n)]
        rr=-1
        for _ in range(remain):
            answer[rr]+=1
            rr-=1
    return answer