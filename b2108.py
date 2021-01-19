#백준 2108번
#통계학

'''
<문제>
수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다.
단, N은 홀수라고 가정하자.

산술평균 : N개의 수들의 합을 N으로 나눈 값
중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
최빈값 : N개의 수들 중 가장 많이 나타나는 값
범위 : N개의 수들 중 최댓값과 최솟값의 차이
N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

<입력>
첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

<출력>
첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
둘째 줄에는 중앙값을 출력한다.
셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
넷째 줄에는 범위를 출력한다.
'''
import sys
from collections import Counter

arithmeticMean = 0
median = 0
mode = 0
scope = 0

num = int(sys.stdin.readline())
nums = []
for i in range(num):
    nums.append(int(sys.stdin.readline()))

#산술평균
arithmeticMean = round(sum(nums) / num)

#중앙값
median = sorted(nums)[num // 2]

#최빈값
#collections Counter() 이용한 풀이 >> 개별값의 빈도수를 dict 형태로 반환
#most_common() 추가 이용
nums.sort()
if len(nums) > 1:
    cnt_nums = Counter(nums).most_common()
    if cnt_nums[0][1] == cnt_nums[1][1]:
        mode = cnt_nums[1][0]
    else:
        mode = cnt_nums[0][0]
else:
    mode = nums[0]

'''
#dictionary 이용한 풀이
counter = {}
for n in nums:
    if n not in counter:
        counter[n] = 0
    counter[n] += 1

max_num = max(counter.values())
max_li = []
for key, value in counter.items():
    if value == max_num:
        max_li.append(key)

mode = max_li[0]
if len(max_li) > 1:
    mode = sorted(max_li)[1]
'''

'''
#set 이용 풀이 / 시간초과
cnt = 0
mode_li = []
for i in set(nums):
    if nums.count(i) == cnt:
        mode_li.append(i)
    elif nums.count(i) > cnt:
        cnt = nums.count(i)
        mode_li.clear()
        mode_li.append(i)
        mode = i
if len(mode_li) > 1:
    mode = sorted(mode_li)[1]
'''

#범위
scope = abs(max(nums) - min(nums))

print(arithmeticMean)
print(median)
print(mode)
print(scope)