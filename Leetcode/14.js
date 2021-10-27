// Leetcode no.14 easy
// Longest Common Prefix

const longestCommonPrefix = (strs) => {
  const n = strs.length
  let res = ''
  let k = 0
  let currChar = ''
  while (true) {
    let flag = true
    for (let i = 0; i < n; i++) {
      if (i === 0) {
        currChar = strs[i][k]
      } else {
        if (strs[i][k] !== currChar) {
          flag = false
          break
        }
      }
    }

    if (currChar === undefined) break

    if (flag) {
      res += strs[0][k]
      k++
    } else {
      break
    }
  }
    
  return res
}

const strs = ['']
console.log(longestCommonPrefix(strs))