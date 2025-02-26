def solution(scov, K):
    answer=0
    import heapq
    heapq.heapify(scov)
    while scov[0]<K:
        answer+=1
        if len(scov)==1:
            answer=-1
            break
        else:
            m1=scov[0]
            heapq.heappop(scov)
            m2=scov[0]
            heapq.heappop(scov)
            new=m1+m2*2
            heapq.heappush(scov,new)

    
    return answer