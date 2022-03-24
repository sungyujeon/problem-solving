# Programmers
# 가장 큰 수 sort

# TODO: 효율성



# 정확성
from itertools import permutations

def solution(numbers):
    candidates = []
    n = len(numbers)

    perms = list(permutations(numbers, n))
    for perm in perms:
        num = int(''.join(list(map(str, perm))))
        candidates.append(num)

    return str(max(candidates))

numbers = [6, 10, 2]
print(solution(numbers))