# a: 해당 원소를 사용했는지 확인하기위함
# k: a list의 index
# input: n개를 뽑아라

arr = [1,2,3]
N = 3

def perm(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(idx, N):
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx+1)
            arr[idx], arr[i] = arr[i], arr[idx]

perm(0)