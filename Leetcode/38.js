// Leetcode no.38
// count and say

const countSay = (curr, depth, n) => {
  if(depth == n) return curr;

  let next = ''
  let count = 1

  for(let i = 1; i < curr.length; i++) {
    if(curr[i] != curr[i-1]) {
      if(count > 0) {
        next += count.toString()
      }
      next += curr[i-1]
      count = 1
    } else {
      count++
    }
  }
  
  if(count > 0) {
    next += count.toString()
  }
  
  if(curr.length > 0){
    next += curr[curr.length-1]
  }
  
  return countSay(next, depth+1, n)
}

const countAndSay = (n) => {
  if (n == 0) return '1';
  
  return countSay('', 0, n);
}

const n = 4
console.log(countAndSay(n))