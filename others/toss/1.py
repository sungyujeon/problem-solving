# 동명이인


def solution(name_list):
    answer = []
    name_dic = {}

    for name in name_list:
        res = name_dic.get(name)
        if res == None:
            name_dic[name] = 0
            answer.append(name + "A")
        else:
            alpha = chr(res + 66)
            name_dic[name] = res + 1
            answer.append(name + alpha)

    return answer


name_list = ["김비바", "김비바", "이비바", "김토스", "이비바", "김비바"]
print(solution(name_list))
