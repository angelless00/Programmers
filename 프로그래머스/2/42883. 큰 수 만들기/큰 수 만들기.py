def solution(number, k):
    answer = ''
    #num_list=list(number)
    # while k>0:
    #     for idx,num in enumerate(num_list):
    #         if num<num_list[idx+1]:
    #             num_list.remove(num)
    #             k-=1
    #             break
    
    num_list=[]
    for i in number:
        while num_list and num_list[-1]<i and k>0:
            num_list.pop(-1)
            k-=1
        num_list.append(i)
    
    # list 문자화
    for i in num_list:
        answer+=i
    if k>0: 
        answer=answer[:-1*k]
        
    return answer