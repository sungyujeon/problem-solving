# 백준 4673번
# 셀프 넘버

check = [True] * 10036
check[0] = False

def self_number(number):
    return number + sum(list(map(int, (str(number)))))

for i in range(1, 10001):
    check[self_number(i)] = False

for idx, flag in enumerate(check[:10001]):
    if flag:
        print(idx)