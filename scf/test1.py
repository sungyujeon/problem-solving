
# sys.stdin = open('input.txt', 'r')
import sys
input = sys.stdin.readline


def intToTime(_time):
    def _intToTime(__time):
        if __time < 10:
            return '0' + str(__time)
        else:
            return str(__time)

    hour = _time // 100
    minute = _time % 100
    
    return f'{_intToTime(hour)}:{_intToTime(minute)}'



n = int(input())

start_times = []
end_times = []
for _ in range(n):
    st, et = input().split(' ~ ')
    start_times.append(int(st.replace(':', '')))
    end_times.append(int(et.replace(':', '')))

max_time = max(start_times)
min_time = min(end_times)

if max_time > min_time:
    print(-1)
else:
    res = f'{intToTime(max_time)} ~ {intToTime(min_time)}'
    print(res)
    