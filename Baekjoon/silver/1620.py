# 백준 1620번 S4
# 나는야 포켓몬 마스터 이다솜

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

#도감
monsters = {}
for i in range(1, n+1):
    monsters[i] = input().strip()

# 도감 k,v 반전
monsters_rev = {v:k for k,v in monsters.items()}

def find(pokemon):
    try:
        key = int(pokemon)
        return monsters.get(key)
    except:
        return monsters_rev.get(pokemon)



for _ in range(m):
    pokemon = input().strip()
    print(find(pokemon))