def solution(m, n, puddles):
    answer = 0
    num=[[0 for _ in range(n)] for _ in range(m)]
    num[0][0]=1
    for col in range(m):
        for row in range(n):
            if (col==0) & (row==0):
                num[col][row]=1
            elif [col+1,row+1] not in puddles:  # 물이 없을떄
                if col==0:
                    num[col][row]=num[col][row-1]
                elif row==0:
                    num[col][row]=num[col-1][row]
                else:
                    num[col][row]=num[col-1][row]+num[col][row-1]
            else:
                num[col][row]=0
    answer=num[-1][-1]%1000000007
    return answer
