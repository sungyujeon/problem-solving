# 백준 1992번 S1
# 쿼드 트리

import sys

# sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def check(_li):
    _flag = 0
    _n = len(_li)
    for i in range(_n):
        for j in range(_n):
            if i == 0 and j == 0:
                flag = _li[i][j]
            if _li[i][j] != _flag:
                return False
    return _flag


def quadTree(_li, _n):
    result = '('
    if _n == 1:
        num = _li[0][0]
        if num == 1:
            return '1'
        else:
            return '0'
    else:
        flag = check(_li)
        if flag is False:  # 분할해야
            _n //= 2
            
            di = [0, 0, _n, _n]
            dj = [0, _n, 0, _n]
            
            for i in range(4):
                _i = di[i]
                _j = dj[i]
                
                new_li = []
                for k in range(_i, _i+_n):
                    tmp = []
                    for l in range(_j, _j+_n):
                        tmp.append(_li[k][l])
                    new_li.append(tmp)
                result += quadTree(new_li, _n)

        else:  # 분할하지 않아도 됨
            if flag == 0:
                return '0'
            else:
                return '1'
    
    result += ')'
    return result
            

n = int(input())
li = [list(map(int, input())) for _ in range(n)]

res = quadTree(li, n)
print(res)
