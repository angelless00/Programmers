def solution(user_id, banned_id):
    answer = 0
    #banned=[[] for _ in range(len(banned_id))]
    #import re
    # for idx,ban_pattern in enumerate(banned_id):
    #     pattern=f'^{ban_pattern.replace("*",".")}$'
    #     for id in user_id:
    #         if re.findall(pattern,id):
    #             banned[idx].append(id)
    
    from itertools import permutations
    import re
    
    per=list(permutations(user_id,len(banned_id)))
    for idx,ban_pattern in enumerate(banned_id):
        pattern=f'^{ban_pattern.replace("*",".")}$'
        new_per=per.copy()
        for ban in new_per:
            if not re.match(pattern,ban[idx]):
                per.remove(ban)
    per=[sorted(i) for i in per]
    answer=len(set(map(tuple,per)))
    return answer