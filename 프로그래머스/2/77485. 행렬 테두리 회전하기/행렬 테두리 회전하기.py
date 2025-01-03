def solution(rows, columns, queries):
    answer = []
    matrix=[list(range(1,rows*columns+1))[columns*i:columns*(i+1)] for i in range(rows)]
    for cha in queries:
        m=10000
        start_x=cha[0]-1
        start_y=cha[1]-1
        end_x=cha[2]-1
        end_y=cha[3]-1
        tmp=matrix[start_x][start_y]

        # 왼쪽
        for i in range(start_x,end_x):
            matrix[i][start_y]=matrix[i+1][start_y]
            m=min(m,matrix[i+1][start_y])
        
        # 아래
        for i in range(start_y,end_y):
            matrix[end_x][i]=matrix[end_x][i+1]
            m=min(m,matrix[end_x][i+1])
        
        # 오른쪽
        for i in range(end_x,start_x,-1):
            matrix[i][end_y]=matrix[i-1][end_y]
            m=min(m,matrix[i][end_y])
        
         
        # 위
        for i in range(end_y,start_y,-1):
            matrix[start_x][i]=matrix[start_x][i-1]
            m=min(m,matrix[start_x][i-1])
        matrix[start_x][start_y+1]=tmp
        
        m=min(m,tmp)
        answer.append(m)   

    return answer