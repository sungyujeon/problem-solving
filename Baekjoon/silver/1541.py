# 백준 1541번 S2
# 잃어버린 괄호

# 숫자가 나오면 tmp_num +=
# -가 나오면 -가 나올때까지 그 수들을 모두 더한여 앞 수에서 뺀다
import sys

input = sys.stdin.readline

exp = input().rstrip()

def my_sum(_in):  # 부호 무시하고 모두 더함
    _in = _in.replace('+', ' ')
    _in = _in.replace('-', ' ')

    nums = _in.split()
    return sum(list(map(int, nums)))

res = 0
isMinus = exp.find('-')

if isMinus == -1:  # -가 없음
    res = my_sum(exp)
else:
    exp_pre = exp[:isMinus]
    exp_post = exp[isMinus+1:]
    res = my_sum(exp_pre) - my_sum(exp_post)

print(res)
