import sys
import heapq

sys.stdin = open('input.txt', 'r')
# input = sys.stdin.readline

rates = list(map(float, input().split()))
rates_dict = {
    'A': rates[0],
    'B': rates[1],
    'C': rates[2],
    'D': rates[3],
    'E': rates[4],
}

n, m = map(int, input().split())

status = []
user_rates = []

for i in range(n):
    status.append(list(input().rstrip()))

for i in range(n):
    user_rates.append(list(input().rstrip()))

heapY = []
heapO = []
for i in range(n):
    for j in range(m):
        if status[i][j] == 'Y':  # 아직 안 본 컨텐츠
            heapq.heappush(heapY, (-rates_dict.get(user_rates[i][j]), i, j, user_rates[i][j]))
        elif status[i][j] == 'O':  # 중간까지 본 컨텐츠
            heapq.heappush(heapO, (-rates_dict.get(user_rates[i][j]), i, j, user_rates[i][j]))
        else:  # 본 컨텐츠
            pass
        
heapY.sort(key=lambda x: (x[0], x[1], x[2]))
heapO.sort(key=lambda x: (x[0], x[1], x[2]))
while heapY:
    info = heapq.heappop(heapY)
    print(info[3], -info[0], info[1], info[2])
while heapO:
    info = heapq.heappop(heapO)
    print(info[3], -info[0], info[1], info[2])
