# mergeSort

def mergeSort_methods():
    def merge_recursion(A, p, q, r):
        i = p  # 왼쪽 배열의 시작 idx
        j = q + 1  # 오른쪽 배열의 시작 idx
        tmp = [0] * (r-p+1)

        for k in range(r-p+1):  # r-p+1 병합해야 하는 배열의 길이
            if i <= q and j <= r:
                if A[i] > A[j]:
                    tmp[k] = A[j]
                    j += 1
                else:
                    tmp[k] = A[i]
                    i += 1
            elif j <= r:
                tmp[k] = A[j]
                j += 1
            else:
                tmp[k] = A[i]
                i += 1

        for k in range(r-p+1):
            A[p+k] = tmp[k]

    def merge_loop(A, p, q, r):
        tmp = []
        i = p
        j = q+1

        while i <= q and j <= r:
            if A[i] > A[j]:
                tmp.append(A[j])
                j += 1
            else:
                tmp.append(A[i])
                i += 1
        
        while i <= q:
            tmp.append(A[i])
            i += 1
        
        while j <= r:
            tmp.append(A[j])
            j += 1

        for k in range(r-p+1):
            A[p+k] = tmp[k]
        

    def mergeSort(A, p, r):
        if p < r:
            q = (p+r) // 2
            mergeSort(A, p, q)
            mergeSort(A, q+1, r)

            # merge_recursion(A, p, q, r)
            merge_loop(A, p, q, r)


    li = [5, 2, 1, 3, 6, 4]
    mergeSort(li, 0, len(li)-1)
    print(li)

mergeSort_methods()
    