# 오픈채팅방


def solution(record):
    n = len(record)
    answer = []
    uids = [''] * n
    flags = [False] * n
    dic = {}

    for i in range(n):
        tmp_r = record[i]
        r = tmp_r.split()
        status = r[0]
        uid = r[1]
        uids[i] = uid

        if status == 'Enter':
            dic[uid] = r[2]
            flags[i] = True
        elif status == 'Change':
            dic[uid] = r[2]
            flags[i] = None

    for i in range(n):
        if flags[i] != None:
            nickname = dic.get(uids[i])
            stat = '들어왔습니다.' if flags[i] else '나갔습니다.'

            s = f'{nickname}님이 {stat}'
            answer.append(s)
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
solution(record)