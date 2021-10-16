

def solution(leave, day, holidays):
    if leave > 21:
        return 30

    # check public holidays
    day_idx = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    day_idx = day_idx.index(day)
    flags = [(13 - day_idx) % 7, (12 - day_idx) % 7]
    days = [0 for _ in range(30)]
    for i in range(30):
        if i % 7 in flags:
            days[i] = 1
    
    # check private holidays
    for day in holidays:
        days[day-1] = 1
    
    # calc longest day
    max_total = 0
    total = 0
    start = 0
    end = 0
    while end < 30:
        while leave < 1 and days[end] == 0:
            if days[start] == 0:
                leave += 1
            start += 1
            total -= 1

        if days[end] == 0:
            leave -= 1
        total += 1
        end += 1
        
        if total > max_total:
            max_total = total    
    
    return max_total

leave = 3
day = 'SUN'
holidays = [2, 6, 17, 29]
print(solution(leave, day, holidays))
