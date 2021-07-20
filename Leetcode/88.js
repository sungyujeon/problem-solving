// Leetcode no.88 easy
// Merge Sorted Array

var merge = function(nums1, m, nums2, n) {
  nums1.splice(m, n, ...nums2)
  nums1.sort((a, b) => a - b)
}

const nums1 = [-10,1,2,3,0,0,0]
const nums2 = [2,5,6]
const m = 4
const n = 3

merge(nums1, m, nums2, n)

//splice(start[, deleteCount], ...args) 원본 배열에 대해
// start index 부터 deleteCount 수만큼 삭제하고 ...args 값으로 대체함.
// 원본 배열의 길이 m index 부터 0이므로 n만큼 삭제하고 num2 배열의 값으로 대체하면 num2가 포함된 정렬되지 않은 배열 num1이 됨

// sort 함수 내부적으로 콜백함수에 두 수가 전달되고,
// 두 수가 정렬되어 있으면 -1(음수), 정렬되어 있지 않으면 1(양수), 같으면 0을 반환하므로,
// (a-b) 값을 리턴하는 것과 동일함