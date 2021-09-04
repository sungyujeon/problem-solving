// Leetcode no.17 medium
// Letter Combinations of a Phone Number

const letters = {
  2: ['a', 'b', 'c'],
  3: ['d', 'e', 'f'],
  4: ['g', 'h', 'i'],
  5: ['j', 'k', 'l'],
  6: ['m', 'n', 'o'],
  7: ['p', 'q', 'r', 's'],
  8: ['t', 'u', 'v'],
  9: ['w', 'x', 'y', 'z']
}

const letterCombinations = (digits) => {
  const dfs = (array, depth, n, letter, res) => {
    if (depth > n) {
      res.push(letter)
      return
    }

    const newArray = [...array]
    const currArray = letters[newArray.shift()]
    for (const char of currArray) {
      dfs(newArray, depth+1, n, letter + char, res)
    }
  }

  if (!digits) return []

  const res = []
  const array = digits.split('').map(Number)
  const n = array.length
  
  dfs(array, 1, n, '', res)
  
  return res
};

const digits = ''
console.log(letterCombinations(digits))
