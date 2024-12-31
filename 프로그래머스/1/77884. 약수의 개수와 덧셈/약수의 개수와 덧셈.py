def solution(left, right):
    answer = 0
    for k in range(left,right+1):
        cnt=0
        for i in range(1,int(k**(1/2))):
            if k%i==0:
                cnt+=1
        cnt*=2
        if k**(1/2)==int(k**(1/2)):
            cnt-=1
            answer-=k
        else:
            answer+=k
    return answer