# 백준 5430번 S2
# AC
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    func = input().rstrip()
    n = int(input())
    li = input().rstrip()[1:-1].split(',')
    
    flag= True
    r_cnt = 0
    d_cnt = 0

    left_cnt = 0
    right_cnt = 0

    i = 0
    while i < len(func):
        if func[i] == 'R':  # R일 때
            while i < len(func) and func[i] == 'R':
                i += 1
                r_cnt += 1
            if r_cnt % 2:
                flag = not flag
            r_cnt = 0

        else:  # D일 때
            while i < len(func) and func[i] == 'D':
                i += 1
                d_cnt += 1
            
            if flag:
                left_cnt += d_cnt
            else:
                right_cnt += d_cnt
            d_cnt = 0

    if (left_cnt + right_cnt) > n:
        print('error')
    else:
        if right_cnt:
            res = li[left_cnt:-right_cnt]
        else:
            res = li[left_cnt:]

        if not flag:
            res.reverse()
        
        res = '[' + ','.join(res) + ']'
        
        print(res)
    
