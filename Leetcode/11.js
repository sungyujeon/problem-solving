// Leetcode no.11 medium
// Container With Most Water

var maxArea2 = function(height) {
  let max = 0

  for (let i = 0; i < height.length - 1; i++) {
    for (let j = i+1; j < height.length; j++) {
      const w = j - i
      const h = Math.min(height[i], height[j])
      
      const area = w * h
      if (area > max) {
        max = area
      }
    }
  }
  
  return max
};

var maxArea = function(height) {
  let max = 0
  let l = 0
  let r = height.length - 1
  
  while (l < r) {
    const w = r - l
    const lh = height[l], rh = height[r]
    const h = Math.min(lh, rh)

    const area = w * h
    max = Math.max(max, area)

    if (lh < rh) {
      l++
    } else {
      r--
    }
  }

  return max
}

const res = maxArea([1,2,1])
console.log(res)