


# 순열: 순서 고려   permutation
# 조합: 순서 고려 x combination

import math
from itertools import permutations, combinations, product, combinations_with_replacement
from collections import Counter
data = ['a', 'b', 'c']

# res = list(combinations(data, 2))
# print(res)
# res = list(permutations(data))
# print(res)


res = list(product(data, repeat=2))
print(res)

res = list(combinations_with_replacement(data, 2))


counter = Counter(['red', 'blue', 'blue'])

# print(counter['red'])
# print(counter['blue'])

def lcm(a, b):
    return a * b // math.gcd(a, b)
print(math.gcd(2, 4))
print(lcm(10, 5))
