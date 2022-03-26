import re

def isValid(log):
    t = "team_name"
    a = "application_name"
    e = "error_level"
    m = "message"

    # log 길이 100
    if len(log) > 100:
        return False

    res = re.findall(f'{t}|{a}|{e}|{m}', log)
    if len(res) != 4:
        return False

    words = re.split(f'{t}|{a}|{e}|{m}', log)
    # 앞 뒤 공백
    if words[0] or words[-1][-1] == ' ':
        return False
    
    words[-1] += ' '
    # value 분리
    words = words[1:]
    for word in words:
        # prefix ' : '
        if word[:3] != ' : ':
            return False
        word = word[3:]

        # 앞 뒤 공백 하나
        if word[0] == ' ' or word[-1] != ' ' or word[-2] == ' ' :
            return False
        word = word[:-1]

        # word valid check
        if not word.isalpha():
            return False
        
    return True
    
    


def solution(logs):
    answer = 0

    for log in logs:
        flag = isValid(log)
        print(flag, log)
        # if not isValid(log):
        #     print(log)
        #     answer += 1

    return answer

logs = ["team_name : db application_name : dbtest error_level : info message : test", 
" team_name : db application_name : dbtest error_level : info message : test", 
"team_name : db application_name : dbtest error_level : info message : test ", 
"team_name  : db application_name : dbtest error_level : info message : test", 
"team_name : db application_name  : dbtest error_level : info message  : test", 
"team_name : db application_name : dbtest error_level : info message : test$", 
" team_name : db application_name : dbtest error_level : info message : test ", 
"team_nam : db application_name  error_level : ", 
"team_name : test application_name : I DONT CARE error_level : error message : x", 
"team_name : ThisIsJustForTest application_name : TestAndTestAndTestAndTest error_level : test message : IAlwaysTestingAndIWillTestForever", 
"team_name : oberervability application_name : LogViewer error_level : error"]
print(solution(logs))