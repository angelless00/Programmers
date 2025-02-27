def solution(n, computers):
    from collections import deque
    
    answer = 0
    visited=[False]*n
    
    def bfs(graph,start,visited):
        que=deque([start])
        while que:
            now=que.popleft()
            for idx,com in enumerate(graph[now]):
                if com==1:
                    if visited[idx]==False:    
                        visited[idx]=True
                        que.append(idx)
        return visited
    for i in range(n):
        for idx,v in enumerate(visited):
            if v==False:
                visited=bfs(computers,idx,visited)
                answer+=1
                
        
    
    return answer