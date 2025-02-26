def solution(array, commands):
    answer = []
    for num_list in commands:
        ar=array[num_list[0]-1:num_list[1]]
        answer.append(sorted(ar)[num_list[2]-1])
    return answer