def solution(n,a,b):
    answer = 0
    import math
    while a!=b:
        a=math.ceil(a/2)
        b=math.ceil(b/2)
        answer+=1

    return answer