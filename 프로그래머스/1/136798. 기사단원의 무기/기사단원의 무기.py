def solution(number, limit, power):
    answer = 0
    power_list=[]
    # 약수 구하기 최적화 해보기
    # for i in range(1,number+1):
    #     cnt=0
    #     for k in range(1,i+1):
    #         if i%k==0:
    #             cnt+=1
        
    for i in range(1,number+1):
        cnt=0
        for k in range(1,int((i+1)**(1/2)+1)):
            if i%k==0:
                cnt+=1
        cnt*=2
        if i**(1/2)==int(i**(1/2)):
            cnt-=1
        
        
        if cnt<=limit:
            power_list.append(cnt)
        else:
            power_list.append(power)
        
    answer=sum(power_list)
    return answer