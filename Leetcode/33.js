// Leetcode no.33 medium
// Search in Rotated Sorted Array


// 1) mid 보다 작고 left 보다 크거나 같을 때
const binary_search = (array, target) => {
  let l = 0
  let r = array.length-1

  while (l <= r) {
    const mid = (l + r) / 2 | 0
    const left_num = array[l]
    const right_num = array[r]
    const mid_num = array[mid]

    if (left_num === target) {
      return l
    } else if (right_num === target) {
      return r
    } else if (mid_num === target) {
      return mid
    }

    if (left_num < mid_num) {
      if (left_num <= target && target < mid_num) {
        r = mid - 1
      } else {
        l = mid + 1
      }
    } else if (mid_num < right_num) {
      if (mid_num < target && target <= right_num) {
        l = mid + 1
      } else {
        r = mid - 1
      }
    } else {
      return -1
    }
  }
  return -1
}

var search = function(nums, target) {
  const res = binary_search(nums, target)
  return res
}

const nums = [3, 1]
const target = 1
console.log(search(nums, target))
