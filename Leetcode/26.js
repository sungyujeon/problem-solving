// Leetcode no.26 Easy
// Remove Duplicates from Sorted Array

var removeDuplicates = function(nums) {
  let k = 0
  const num_set = new Set([])
  
  for (let i = 0; i < nums.length; i++) {
      const num = nums[i]
      
      if (!num_set.has(num)) {
          num_set.add(num)
          nums[k] = num 
          k++
      }
  }
  
  return k
}

const nums = [0,0,1,1,1,2,2,3,3,4]
console.log(removeDuplicates(nums))
console.log(nums)