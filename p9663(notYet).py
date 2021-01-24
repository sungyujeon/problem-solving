# 백준 9663번
# N-Queen

'''
<문제>
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

<입력>
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

<출력>
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.
'''

# N == 1: 1
# N == 2: 0
# N == 3: 0
# N == 4: 


N = int(input())
check = []
for i in range(N):
    check_tmp = []
    for j in range(N):
        check_tmp.append(True)
    check.append(check_tmp)
queen_loc = []
for i in range(N):
    queen_loc_tmp = []
    for j in range(N):
        queen_loc_tmp.append(False)
    queen_loc.append(queen_loc_tmp)
cnt = 0
depth = 0
# (i, j)에 놓였을 때 (x축 == i) 또는 (y축 == j) 또는 (x축 + y축 == i + j) >> False로 바꿈
cnt_queen = []

def queen():
    global check
    global queen_loc
    global cnt
    global depth
    global cnt_queen

    if depth == 4:
        if not cnt:
            cnt -= 1
            return

    
    for i in range(N):
        for j in range(N):
            # if depth == 0:
            #     check[i][j] = False
            #     queen_loc[i][j] = True
            if check[i][j]:
                queen_loc[i][j] = True
                check[i][j] = False

            if queen_loc[i][j]:
                for n in range(N):
                    for m in range(N):
                        if not check[n][m]:
                            continue
                        elif i == n or j == m or (n+m == i + j + 2*n):
                            check[n][m] = False
                            cnt_queen.append((n, m))
                
                # queen 말 추가
                depth += 1
                queen()

                # queen 말 제거
                queen_loc[i][j] = False
                for t in cnt_queen:
                    check[t[0]][t[1]] = True

queen()

print(cnt)