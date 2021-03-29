# 백준 12871번 S5
# 무한 문자열
import sys
from math import gcd
input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()


s1_len = len(s1)
s2_len = len(s2)
_lcm =  (s1_len * s2_len) // gcd(s1_len, s2_len)

s1 = s1 * (_lcm // s1_len)
s2 = s2 * (_lcm // s2_len)

if s1 == s2:
    print(1)
else:
    print(0)

# def isSingleWord(_s):
#     flag = _s[0]
#     for i in _s:
#         if i != flag:
#             return False
#     return True

# def repeatStr(_s):
#     if isSingleWord(_s):
#         return _s[0]
    
#     l = len(_s)
#     if l % 2:  # 홀수이면
#         return _s
#     else:  # 짝수이면
#         while True:  # 여기서 반례가 있구나 ababab / abababab
#             _s1 = _s[:l//2]
#             _s2 = _s[l//2:]

#             if _s1 == _s2:
#                 _s = _s[:l//2]
#             else:
#                 return _s


# def isSame(_s1, _s2):
#     k = len(_s1)
#     si = -k
#     ei = 0

#     while True:
#         si = ei
#         ei += k
        
#         if _s2[si:ei] != _s1:
#             return False
        
#         if ei == len(_s2):
#             return True


# s1 = input().rstrip()
# s2 = input().rstrip()

# res = 0
# if len(s1) < len(s2):
#     s1 = repeatStr(s1)
    
#     if isSame(s1, s2):
#         res = 1
# else:
#     s2 = repeatStr(s2)

#     if isSame(s2, s1):
#         res = 1

# print(res)

