def solution(n, works):
    answer=0
    works=[-1*n for n in works]
    import heapq
    heapq.heapify(works)

    for _ in range(n):
        work=heapq.heappop(works)
        if work==0:
            break
        else:
            work+=1
            heapq.heappush(works,work)
        
    print(works)
    for i in works:
        answer+=(i)**2
        
    return answer
    
        
            
            