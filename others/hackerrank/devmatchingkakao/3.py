# hackerrank 카카오엔터 3번
# Binary Manipulation

def isZero(ar):
    for a in ar:
        if a == '1':
            return False
    return True

def setBinary(arr, n, arr_set, tmp_arr):
    for i in range(n-1):
        newArr = list(arr)
        if newArr[i+1] == 1:
            flag = True
            if i+1 == n-1:
                if newArr[n-1] != 1:
                    flag = False
            else:
                for j in range(i+2, n):
                    if newArr[j] != 0:
                        flag = False
                        break
            
            if flag:
                newArr[i] = 1 if newArr[i] == 0 else 0
            else:
                newArr[n-1] = 1 if newArr[n-1] == 0 else 0
        else:
            newArr[n-1] = 1 if newArr[n-1] == 0 else 0
        
        arr_bi = ''.join(list(map(str, newArr)))
        
        # check
        if isZero(arr_bi):
            return True
        
        if arr_bi not in arr_set:
            arr_set.add(arr_bi)
            tmp_arr.append(newArr)
    
    return False
                
        

def minOperations(n):
    base_bi = bin(n)[2:]
    cnt = 1
    array = list(map(int, list(base_bi)))
    n = len(array)
    arr_set = set([base_bi])
    curr_arr = [array]

    while curr_arr:
        tmp_arr = []
        flag = setBinary(curr_arr.pop(), n, arr_set, tmp_arr)

        if flag:
            return cnt

        if tmp_arr and not curr_arr:
            curr_arr = tmp_arr
            cnt += 1
    
    return cnt

n = 13
print(minOperations(n))