# 백준 1439번 S5
# 뒤집기

# 모두 같은 수이면 0 반환
# 같지 않으면 min(1을 뒤집는 횟수, 0을 뒤집는 횟수) 반환



s = input()

test1 = s.replace('1', ' ').split()
test2 = s.replace('0', ' ').split()

print(min(len(test1), len(test2)))

