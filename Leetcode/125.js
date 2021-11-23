// Leetcode no.125
// Valid Palindrome

var isPalindrome = function(s) {
  s = s.replace(/[^0-9a-zA-Z]+/gmi,"")
  s = s.toLowerCase()
  var l = 0, r = s.length - 1

  while(l<r) {
      if(s.charAt(l) != s.charAt(r)) {
          return false
      }
      l++
      r--
  }
  return true
}

s = "A man, a plan, a canal: Panama"
console.log(isPalindrome(s))