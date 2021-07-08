// Leetcode no.389
// Find the difference

var findTheDifference = function(s, t) {
    s = s.split('').sort()
    t = t.split('').sort()

    for (let i = 0; i < t.length; i++) {
      if (i == t.length-1) {
        console.log(s[i])
        return t[i]
      }

      if (s[i] !== t[i]) {
        return t[i]
      }
    }
};

console.log(findTheDifference('a', 'aa'))