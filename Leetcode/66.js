// Leetcode no.66 easy
// Plus One

var plusOne = function(digits) {
  let flag = false
  let i = digits.length - 1
  
  while (i >= 0) {
    if (digits[i] === 9) {
      digits[i] = 0
      i--
    } else {
      digits[i] += 1
      return digits
    }
  }
  digits = [1].concat(digits)
  return digits
};  

const digits = [0]
const res = plusOne(digits)
console.log(res)