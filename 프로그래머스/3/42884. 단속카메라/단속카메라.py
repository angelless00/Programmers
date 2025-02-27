def solution(routes):
    answer = 0
    routes=sorted(routes,key=lambda x:x[1])
    while routes:
        cam=routes.pop(0)[1]
        answer+=1
        routes=[route for route in routes if route[0]>cam]
    
    return answer