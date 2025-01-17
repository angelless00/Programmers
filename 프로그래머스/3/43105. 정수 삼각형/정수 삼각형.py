def solution(triangle):
    triangle=triangle[::-1] # 삼각형 뒤집기
    for floor in range(1,len(triangle)):
        for i in range(len(triangle[floor])):
            triangle[floor][i]+=max(triangle[floor-1][i],triangle[floor-1][i+1])
    answer=triangle[-1][0]    
    return answer
