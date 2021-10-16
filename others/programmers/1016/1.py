# 2021 데브매칭 하반기

def setNewId(id):
    num_idx = -1
    for i in range(len(id)):
        if id[i].isdigit():
            num_idx = i
            break
    
    if num_idx == -1:
        return id + '1'

    S = id[:num_idx]
    N = int(id[num_idx:]) + 1
    return S + str(N)

def solution(registered_list, new_id):
    answer = ''
    registered_set = set(registered_list)

    if new_id not in registered_set:
        answer = new_id
    else:
        while new_id in registered_set:
            new_id = setNewId(new_id)
        answer = new_id

    return answer


registered_list = ["card", "ace13", "ace16", "banker", "ace17", "ace14"]
new_id = 'ace15'
print(solution(registered_list, new_id))