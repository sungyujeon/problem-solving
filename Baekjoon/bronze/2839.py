# 백준 2839번
# 설탕 배달

# 3kg, 5kg 봉지로 n(g)의 설탕을 넣어야 함
# 1. n % 5 == 0 >> min = n // 5
# 2. n % 5 in [1, 3] >> min = n // 5 + 1
# 3. n % 5 in [2, 4] >> min = n // 5 + 2
n = int(input())

def min(kg):
    min = 0
    if kg in [4, 7]:
        min = -1
    else:
        if kg % 5 == 0:
            min = kg // 5
        elif kg % 5 in [1, 3]:
            min = kg // 5 + 1
        else:
            min = kg // 5 + 2
    return min

print(min(n))