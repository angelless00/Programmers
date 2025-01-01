def solution(arr1, arr2):
    answer = []
    row=len(arr1)
    column=len(arr1[0])
    for r in range(row):
        rr=[]
        for c in range(column):
            rr.append(arr1[r][c]+arr2[r][c])
        answer.append(rr)
    
    return answer