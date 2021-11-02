// Leetcode no.28 easy
// Implement strStr()

// const strStr = (haystack, needle) => {
//   const res = haystack.indexOf(needle)
//   return res
// }

const strStr = (haystack, needle) => {
  if (!needle) return 0
  if (!haystack) return -1

  const n = needle.length
  for (let i = 0; i < haystack.length - n + 1; i++) {
    const tmp_str = haystack.substring(i, i+n)
    if (needle === tmp_str) {
      return i
    }
  }
  return -1
}

const haystack = ''
const needle = ''
console.log(strStr(haystack, needle))