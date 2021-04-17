def z_key(k):
    divisor = k % z
    count = k // z
    dp_divisor = dp[divisor]
    if dp_divisor == -1:
        dp_divisor = 987654321
    return count + dp_divisor

def multiple_key(k):
    li = list(r_dict_keys)
    li.sort(reverse=True)
    
    for num in li:
        if k % curr_loc_key == 0:
            count = 1 + 2 * (k // num)
        else:
            if k % num == 0:
                count = 2 + 2 * (k // num)
    return count


n = 5
z = 5
roads = [[1,2,3], [0,3,2]]
queries = [0,1,2,3,4,5,6]
l_queries = len(queries)
r_dict = {}
curr_loc_key = 0
for road in roads:
    a, b, c = road
    r_dict[c] = (a, b)
    if a == 0:
        curr_loc_key = c

dp = [0] * l_queries
dp[0] = 0
answer = [0] * l_queries
for i in range(l_queries):
    key = queries[i]
    total = 0
    curr_loc = 0
    r_dict_keys = r_dict.keys()
    min_key = min(r_dict_keys)
    if key == 0:
        answer[i] = 0
    elif key == z:
        answer[i] = 1
        dp[z] = 1
    else:
        if key in r_dict_keys:
            if key == curr_loc_key:
                answer[i] = 1
                dp[key] = 1
            else:
                answer[i] = 2
                dp[key] = 2
        else:
            if key < min_key:
                answer[i] = -1
                dp[key] = -1
            else:  # 그 이외의 key들에 대해서
                dp[key] = min(z_key(key), multiple_key(key))
                answer[i] = dp[key]
print(answer)
    