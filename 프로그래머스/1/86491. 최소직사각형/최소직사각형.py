def solution(sizes):
    m=0
    M=0
    for size in sizes:
        m=max(m,min(size))
        M=max(M,max(size))
    return m*M