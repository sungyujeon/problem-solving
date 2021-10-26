# hackerrank 카카오엔터 1번
# cardinality sorting

def cardinality(nums):
    def getCardinality(num):
        bi_num = bin(num)
        print(bi_num)
        cnt = 0
        for k in range(2, len(bi_num)):
            if bi_num[k] == '1':
                cnt += 1
        return (cnt, num)

    n = len(nums)
    bi_nums = [None] * n
    for k in range(n):
        bi_nums[k] = getCardinality(nums[k])

    bi_nums.sort()
    nums = list(map(lambda x: x[1], bi_nums))
    
    return nums


nums = [1,2,3,4]
print(cardinality(nums))