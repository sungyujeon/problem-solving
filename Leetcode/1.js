// Leetcode no.1 easy
// Two Sum

var twoSum = function(nums, target) {
  const map = new Map()
  
  for (let i = 0; i < nums.length; i++) {
    const n = nums[i]
    const m = target - n

    if (map.has(m)) {
      return [map.get(m), i]
    }
    
    if (!map.has(n)) {
      map.set(n, i)
    }
  }
};

const nums = [2,7,11,15]
const target = 9
console.log(twoSum(nums, target))