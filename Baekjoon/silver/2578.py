# 백준 2578번 S5
# 빙고


def isBingo(_arr):
    cnt = 0
    for i in range(5):
        for j in range(5):
            if not _arr[i][j]:  # False가 있으면
                break
        else:
            cnt += 1

            if cnt > 2:
                return True
    
    for i in range(5):
        for j in range(5):
            if not _arr[j][i]:  # False가 있으면
                break
        else:
            cnt += 1

            if cnt > 2:
                return True

    # 대각선
    for i in range(5):
        if not _arr[i][i]:
            break
    else:
        cnt+= 1
        if cnt > 2:
            return True

    # 대각선
    for i in range(5):
        if not _arr[i][4-i]:
            break
    else:
        cnt+= 1
        if cnt > 2:
            return True
    return False




puzzle = [list(input().split()) for _ in range(5)]
puzzle_flag = [[False] * 5 for _ in range(5)]

def check_bingo(_num):
    global puzzle
    global puzzle_flag

    for i in range(5):
        for j in range(5):
            if puzzle[i][j] == _num:
                puzzle_flag[i][j] = True
                return


tmp_announce = ''
for _ in range(5):
    tmp_announce += input() + ' '

announce = list(tmp_announce.split())


# 번호 부르기
for i in range(25):
    num = announce[i]  # 부르는 수
    check_bingo(num)

    if i > 10:  # 10번 넘을 때부터 빙고 검사
        if isBingo(puzzle_flag):
            print(i+1)
            break


# puzzle = [
#     ['11','12','2','24','10'],
#     ['16','1','13','3','25'],
#     ['6','20','5','21','17'],
#     ['19','4','8','14','9'],
#     ['22','15','7','23','18'],    
# ]

# announce = ['5','10','7','16','2','4','22','8','17','13','3','18','1','6','25','12','19','23','14','21','11','24','9','20','15']