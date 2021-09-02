// Leetcode no.13 easy
// Roman to Integer

// IV IX XL XC CD CM

const roman = new Map([
  ['I', 1],
  ['V', 5],
  ['X', 10],
  ['L', 50],
  ['C', 100],
  ['D', 500],
  ['M', 1000],
  ['IV', 4],
  ['IX', 9],
  ['XL', 40],
  ['XC', 90],
  ['CD', 400],
  ['CM', 900] 
])

const romanToInt = (s) => {
  const regex = /IV|IX|XL|XL|XC|CD|CM|\S/g
  const array = s.match(regex)
  
  let total = 0
  for (const char of array) {
    total += roman.get(char)
  }
  
  return total
}

const s = 'MCMXCIV'
romanToInt(s)