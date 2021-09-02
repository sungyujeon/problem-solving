

const solution = (table, languages, preference) => {
  const occupations = new Map()
  table = table.map((ele) => ele.split(' '))
  
  for (let i = 0; i < languages.length; i++) {
    for (const t of table) {
      const ocpn = t[0]
      const idx = t.indexOf(languages[i])

      if (i === 0) {
        occupations.set(ocpn, 0)
      }

      if (idx !== -1) {
        const curr_score = occupations.get(ocpn)
        const next_score = (6 - idx) * preference[i]
        occupations.set(ocpn, curr_score + next_score)
      }
    }
  }

  // sort
  const sortedArray = [...occupations.entries()].sort().sort((a, b) => b[1] - a[1])
  const res = sortedArray[0][0]

  return res
}

const table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
const languages = ["PYTHON", "C++", "SQL"]
const preference = [7, 5, 5]
solution(table, languages, preference)