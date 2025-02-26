def solution(bridge_length, weight, truck_weights):
    trucks=[truck_weights[0]]
    seconds=[1]
    sec=1
    idx=0
    while (trucks!=[]) :
        sec+=1
        # 이미 지나간 트럭 빼기
        if seconds[0]==bridge_length:
            seconds.pop(0)
            trucks.pop(0)
        seconds=[i+1 for i in seconds]
        if idx!= len(truck_weights)-1:
            if sum(trucks)+truck_weights[idx+1]<=weight:
                seconds.append(1)
                trucks.append(truck_weights[idx+1])
                idx+=1

            
    return sec