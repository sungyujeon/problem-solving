# 백준 2468번
# 안전 영역

N = int(input())
cnt = 0
height = []
safe_zone = [[True for _ in range(N)] for _ in range(N)]
for _ in range(N):
    height.append(list(map(int, input().split())))

# max_height
max_height_list = []
for h in height:
    max_height_list.append(max(h))
max_height = max(max_height_list)

# 1부터 max_height까지 물에 잠기는 지역은 False 처리
for i in range(1, max_height+1):
    for m in range(N):
        for n in range(N):
            if height[m][n] <= i:
                safe_zone[m][n] = False
    # 검증하는 함수 실행
    safe((0, 0))
depth = 0
def safe(safe_tuple):
    global cnt
    global depth
    if safe_zone[safe_tuple[0]][safe_tuple[1]]:
        safe_zone[safe_tuple[0]][safe_tuple[1]] = False
        if safe_tuple[1] == N-1:
            pass
        elif safe_tuple[1] < N -1:
            safe((safe_tuple[0], safe_tuple[1]))
    else:
        if depth == 0:
            safe()
        cnt += 1