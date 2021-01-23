# 백준 15649번
# N과 M(1)

'''
<문제>
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

<입력>
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

<출력>
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''
import sys

N, M = map(int, sys.stdin.readline().split())

check_list = [False] * N
out = []

def sequence():
    if len(out) == M:
        print(*out)
        return

    for i in range(N):
        if not check_list[i]:
            out.append(i+1)
            check_list[i] = True
            
            sequence()

            out.pop()
            check_list[i] = False
sequence()

# 함수의 호출 스택을 이용한 풀이
'''
n, m = map(int, input().split())

def f(s):
  if len(s) == m:
    print(' '.join(map(str, s)))
    return

  for i in range(1, n + 1):
    if i in s:
      continue
    f(s + [i])

f([])
'''
