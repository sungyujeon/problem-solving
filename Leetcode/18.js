// Leetcode no.18 medium
// 4Sum

var fourSum = function(nums, target) {

  const dfs = (depth, idx, total, li) => {
    if (depth < 2) {
      let i = idx
      while (i < nums.length + depth - 3) {
        dfs(depth+1, i+1, total+nums[i], li.concat([nums[i]]))
        i++
        
        while (nums[i] === nums[i-1]) i++
      }
    } else {
      let i = idx
      let j = nums.length - 1

      while (i < j) {
        const tmp = [nums[i], nums[j]]
        let tmp_total = total + tmp[0] + tmp[1]
        
        if (tmp_total < target) {
          i++
        } else if (tmp_total > target) {
          j--
        } else {
          const tmp = [nums[i], nums[j]]
          res.push(li.concat(tmp))
          while (i < j && nums[i] === tmp[0]) i++
          while (i < j && nums[j] === tmp[1]) j--
        }
      }
    }
  }
  
  const res = []
  nums.sort((a, b) => a - b)
  dfs(0, 0, 0, [])
  
  return res
};
const nums = [1,0,-1,0,-2,2]
const target = 0
const res = fourSum(nums, target)
console.log(res)