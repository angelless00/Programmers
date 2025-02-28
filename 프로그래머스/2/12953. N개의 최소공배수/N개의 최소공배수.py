def solution(arr):
    answer = 0
    stop=False
    arr=sorted(arr)
    n=arr[-1]
    for a in range(1,1000000):
        for i in arr:
            if (a*n)%i!=0:
                break
            if i==n:
                answer=a*n
                stop=True
        if stop==True:
            break

        
    return answer