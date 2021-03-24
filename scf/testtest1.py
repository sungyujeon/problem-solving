import sys

sys.stdin = open('input.txt', 'r')

N = int(input())

st_hour = -1 # 0
st_min = -1 # 0
en_hour = 25
en_min = 60

result = -1

for n in range(N):
    check = 0  #
    time = input()
    if n == 0:  # 아하
        check = 1
        st_hour = time[:2]
        st_min = time[3:5]
        en_hour = time[8:10]
        en_min = time[11:13]
    else:
        # 시작시간이 첫 시간 사이에 있는 경우
        if int(st_hour) <= int(time[:2]) and int(st_min) <= int(time[3:5]) and int(time[:2]) <= int(en_hour) and int(time[3:5]) <= int(en_min):
            st_hour = time[:2]
            st_min = time[3:5]
            check = 1
        # 끝 시간이 사이에 있는 경우
        if int(st_hour) <= int(time[8:10]) and int(st_min) <= int(time[11:13]) and int(time[8:10]) <= int(en_hour) and int(time[11:13]) <= int(en_min):
            en_hour = time[8:10]
            en_min = time[11:13]
            check = 1
    if check == 0:
        break

if st_hour == en_hour and st_min == en_min:
    print(-1)
elif check:
    print(f'{st_hour}:{st_min} ~ {en_hour}:{en_min}')
else:
    print(result)