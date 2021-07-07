// Leetcode no.242 easy
// Valid Anagram

var isAnagram = function(s, t) {
  const lenS = s.length
  const lenT = t.length
  const array = Array(26).fill(0)
  
  if (lenS !== lenT) {
    return false
  }

  for (let i = 0; i < lenS; i++) {
    const idx = s[i].charCodeAt(0) - 97
    array[idx]++
  }
  for (let i = 0; i < lenT; i++) {
    const idx = t[i].charCodeAt(0) - 97
    
    if (array[idx] > 0) {
      array[idx]--
    } else {
      return false
    }
  }

  const res = !array.reduce( (accumulator, currentValue) => accumulator + currentValue )
  return res
}

console.log(isAnagram('rat', 'tar'))

