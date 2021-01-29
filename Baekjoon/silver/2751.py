# 백준 2751번 S5
# 수 정렬하기2
# 시간복잡도 O(nlogn) 정렬 알고리즘으로 풀기
# (병합 정렬, 힙 정렬 등으로 풀기)
import sys
N = int(sys.stdin.readline())

num_list = []
for _ in range(N):
    num_list.append(int(sys.stdin.readline()))

num_list.sort()
for number in num_list:
    print(number)