# 백준 1244번 S4
# 스위치 켜고 끄기
import sys

input = sys.stdin.readline

switch_n = int(input())
switch = [-1] + list(map(int, input().split()))

st_n = int(input())
students = []
for _ in range(st_n):
    a, b = map(int, input().split())
    students.append((a,b))
    
for i in students:
    if i[0] == 1:  # 남자
        male_range = switch_n // i[1]
        male_list = [i[1] * k for k in range(1, male_range+1)]
        
        for male_num in male_list:
            switch[male_num] = 0 if switch[male_num] else 1
    else:  # 여자
        female_num = i[1]
        switch[female_num] = 0 if switch[female_num] else 1
            
        female_range = min(female_num-1, switch_n - female_num)

        for j in range(1, female_range+1):
            if switch[female_num-j] == switch[female_num+j]:
                switch[female_num-j] = 0 if switch[female_num-j] else 1
                switch[female_num+j] = 0 if switch[female_num+j] else 1
            else:
                break

result_list = switch
result = ''
for i in range(1, switch_n+1):
    result += str(result_list[i]) + ' '
    if not i % 20:
        result = result[:-1] + '\n'
    elif i == len(result_list):
        result = result[:-1]
print(result)