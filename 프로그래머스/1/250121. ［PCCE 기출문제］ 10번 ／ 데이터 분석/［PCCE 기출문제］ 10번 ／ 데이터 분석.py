def solution(data, ext, val_ext, sort_by):
    def code(name):
        if name=='code':
            c=0
        elif name=='date':
            c=1
        elif name=='maximum':
            c=2
        elif name=='remain':
            c=3
        return c
    
    answer=sorted([d for d in data if d[code(ext)]<val_ext],key=lambda d:d[code(sort_by)])
    
    return answer