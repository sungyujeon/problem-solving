# 백준 1966번 S3
# 프린터 큐

import sys
input = sys.stdin.readline

def queue(m, imp, imp_tuple):
    # imp_tuple이 빌 때까지 반복
    # imp_tuple[0][1]이 max(imp)와 같다면, imp.remove(imp_tuple[0][1]) && imp_tuple.pop(0) && cnt +=1
    # 이 때 imp_tuple[0][0] == m: break
    # 아니라면, imp_tuple.append(imp_tuple.pop(0))
    cnt = 0
    while imp:
        if imp_tuple[0][1] == max(imp):
            if imp_tuple[0][0] == m:
                cnt += 1
                break
            else:
                imp.remove(imp_tuple[0][1])
                imp_tuple.pop(0)
                cnt += 1
        else:
            imp_tuple.append(imp_tuple.pop(0))
    return cnt

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    idx = [i for i in range(n)]
    
    imp = list(map(int, input().split()))
    imp_tuple = list(zip(idx, imp))

    print(queue(m, imp, imp_tuple))
    
