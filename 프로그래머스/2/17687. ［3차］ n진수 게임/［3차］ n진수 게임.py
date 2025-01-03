def solution(n, t, m, p):
    answer = ''
    num_list='0'
    nums=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(t*m):
        num=''
        while i>0:
            remain=i%n
            i=i//n
            num=nums[remain]+num
        num_list+=num
        if len(num_list)>t*m:
            break
    answer=num_list[p-1::m][:t]
            
        

        
    return answer