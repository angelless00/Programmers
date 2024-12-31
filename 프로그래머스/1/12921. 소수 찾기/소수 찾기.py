def solution(n):
    answer = 0
    # for i in range(2,n+1):
    #     cnt=0
    #     for j in range(1,int((i)**(1/2))+1):
    #         if i%j==0:
    #             cnt+=1
    #     if cnt==1:
    #         answer+=1
    # 효율성에서 실패
    # 전체에서 각수의 배수들을 뺴는 방법으로 진행
    
    prime_nums=set(range(2,n+1))
    for i in range(2,int((n)**0.5)+1):
        prime_nums-=set(range(i*2,n+1,i))
    answer=len(prime_nums)
    return answer