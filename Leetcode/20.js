// Leetcode no.20 easy
// Valid Parentheses

const isValid = (s) => {
  let res = true

  const inEle = ['(', '{', '[']
  const outEle = [')', '}', ']']

  const stack = []

  for (let i = 0; i < s.length; i++) {
    if (inEle.indexOf(s[i]) !== -1) {  // ins
      stack.push(s[i])
    } else {  // outs
      if (!stack) return false

      const prevEle = stack[stack.length - 1]
      const prevEleIdx = inEle.indexOf(prevEle)
      const currEleIdx = outEle.indexOf(s[i])

      if (prevEleIdx === currEleIdx) {
        stack.pop()
      } else {
        return false
      }
    }
  }

  if (stack.length !== 0) return false

  return res
}

const s = '()'
console.log(isValid(s))