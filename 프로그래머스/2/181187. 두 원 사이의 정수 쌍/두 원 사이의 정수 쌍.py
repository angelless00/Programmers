def solution(r1, r2):
    answer = 0
    # 시간초과 
    # cnt=0
    # for x in range(1,r2+1):
    #     for y in range(max(r1-x,0),r2+1):
    #         if r1**2<=x**2 +y**2<=r2**2:
    #             cnt+=1
    #         elif x**2+y**2>r2**2:
    #             break
    # answer=cnt*4
    import math 
    for x in range(1,r1+1):
        y2=math.floor((r2**2 - x**2)**(1/2))
        y1=math.ceil((r1**2 - x**2)**(1/2))
        answer+=y2-y1+1
    for x in range(r1+1,r2+1):
        y=math.floor((r2**2 - x**2)**(1/2))
        answer+=y+1
    answer*=4
    return answer