var searchInsert = function(nums, target) {
  
  const binary_search = (left, right, _target, array) => {
    let l = left, r = right

    while (l <= r) {
      const mid = ((l + r) / 2) | 0  // Math.trunc(float_number)
      const m = array[mid]
      if (_target === m) {
        return mid
      } else if (_target < m) {
        r = mid - 1
      } else {
        l = mid + 1
      }
    }
    return l
  }

  return binary_search(0, nums.length-1, target, nums)
}

nums = [1,3,5,6]
target = 2
console.log(searchInsert(nums, target))

