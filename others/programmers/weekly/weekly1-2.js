const getGrade = (score) => {
  let res = 'F'
  if (score >= 90) {
    res = 'A'
  } else if (score >= 80) {
    res = 'B'
  } else if (score >= 70) {
    res = 'C'
  } else if (score >= 50) {
    res = 'D'
  }

  return res
}

const isUnique = (array, score) => {
  let cnt = 0
  for (const _score of array) {
    if (_score === score) {
      cnt++
      if (cnt > 1) {
        return false
      }
    }
  }
  return true
}

const transpose = (array) => {
  return (
    array.reduce(
      (result, row) => {
        return row.map((_, i) => [...(result[i] || []), row[i]])
      },
      []
    )
  )
}

function solution(scores) {
  scores = transpose(scores)

  let answer = ''
  const n = scores.length

  for (let i = 0; i < n; i++) {
    const my_score = scores[i][i]

    if (isUnique(scores[i], my_score)) {
      scores[i].sort((x, y) => x - y)
  
      if (scores[i][0] === my_score) {
        scores[i].splice(0, 1)
      } else if (scores[i][n-1] === my_score) {
        scores[i].splice(n-1, 1)
      }
    }

    const sum = scores[i].reduce((acc, curr) => acc + curr)
    const avg = sum / scores[i].length
    const grade = getGrade(avg)
    answer += grade
  
  }
  return answer
}

const scores = [[100,90,98,88,65],[50,45,99,85,77],[47,88,95,80,67],[61,57,100,80,65],[24,90,94,75,65]]
console.log(solution(scores))