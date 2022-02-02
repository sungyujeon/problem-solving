# 5과목 > 4개 분반

from copy import deepcopy

def solution(schedule):
    answer = 0
    new_schedule = setArray(schedule)
    
    answer = getSchedule(new_schedule)
    print(answer)
    
    
    return

def getSchedule(schedule_list):
    used = [False] * 5
    used_q = [[False] * 4 for _ in range(5)]
    my_schedule = [[] for _ in range(5)]
    
    return dfs(0, 5, used, used_q, my_schedule, schedule_list, 0)
    
def dfs(depth, target, _used, _used_q, curr_schedule, schedule_list, res):
    if depth == target:
        return res+1
    
    for p in range(5):
        if not isUsed(_used_q, p):
            for q in range(4):
                if not _used_q[p][q]:
                    _used_q[p][q] = True
                    
                    _schedule = schedule_list[p][q]
                    if isAvailable(curr_schedule, _schedule):
                        res = dfs(depth+1, target, _used, _used_q, curr_schedule, schedule_list, res)
                        rollback(curr_schedule, _schedule)
                    _used_q[p][q] = False
    return res
              
def isUsed(used, p):
    for i in range(4):
        if used[p][i] == True:
            return False
    return True

def rollback(curr_schedule, _schedule):
    is_single = _schedule[0]
    
    if is_single:
        curr_schedule[_schedule[1]].pop()
    
    else:
        curr_schedule[_schedule[1]].pop()
        curr_schedule[_schedule[4]].pop()
        
                        
def isAvailable(curr_schedule, _schedule):
    is_single = _schedule[0]
    
    if is_single:
        date = _schedule[1]
        start = _schedule[2]
        end = _schedule[3]
        flag = getValid(date, start, end, curr_schedule)
        
        if flag:
            curr_schedule[date].append([start, end])
            
        else:
            return False
    else:
        date1 = _schedule[1]
        start1 = _schedule[2]
        end1 = _schedule[3]
        date2 = _schedule[4]
        start2 = _schedule[5]
        end2 = _schedule[6]
        
        flag1 = getValid(date1, start1, end1, curr_schedule)
        flag2 = getValid(date2, start2, end2, curr_schedule)

        if flag1 and flag2:
            curr_schedule[date1].append([start1, end1])
            curr_schedule[date2].append([start2, end2])
        else:
            return False
    
    return True
            
            
def getValid(_date, _start, _end, _curr_schedule):
    _curr_schedule = deepcopy(_curr_schedule[_date])
    
    while _curr_schedule:
        p_start, p_end = _curr_schedule.pop()
        
        if p_start < _start < p_end or p_start < _end < p_end:
            return False
    
    return True
        
            
    
    
        

def setArray(arr):
    date_dict = {
        'MO': 0,
        'TU': 1,
        'WE': 2,
        'TH': 3,
        'FR': 4
    }
    _arr = deepcopy(arr)
    
    n = len(_arr)
    for i in range(n):
        for j in range(len(_arr[i])):
            day_class = _arr[i][j]
            day_class_list = day_class.split()
            day1 = date_dict.get(day_class_list[0])
            time1 = strToTime(day_class_list[1])
            
            _tmp = []
            if len(day_class_list) > 2:
                day2 = date_dict.get(day_class_list[2])
                time2 = strToTime(day_class_list[3])
                
                _tmp = [False, day1, time1, getEndTime(time1, False), day2, time2, getEndTime(time2, False)]
            else:
                _tmp = [True, day1, time1, getEndTime(time1, True)]   
            
            _arr[i][j] = _tmp
    
    return _arr

def strToTime(t):
    h, m = list(map(int, t.split(':')))
    return h * 100 + m

def getEndTime(t, isSingleClass):
    flag = False
    if t % 100:
        flag = True
        
    if isSingleClass:
        return t + 300
    else:
        if flag:
            return t + 170
        else:
            return t + 130

schedule = [["MO 12:00 WE 14:30", "MO 12:00", "MO 15:00", "MO 18:00"], ["TU 09:00", "TU 10:00", "TU 15:00", "TU 18:00"], ["WE 09:00", "WE 12:00", "WE 15:00", "WE 18:00"], ["TH 09:30", "TH 11:30", "TH 15:00", "TH 18:00"], ["FR 15:00", "FR 15:00", "FR 15:00", "FR 15:00"]]
solution(schedule)

