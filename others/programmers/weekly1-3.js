const transpose = (array) => {
  const row = array.length
  const col = array[0].length
  const newArray = Array.from(Array(col), () => new Array(row).fill(0))

  for (let i = 0; i < col; i++) {
    for (let j = 0; j < row; j++) {
      newArray[i][j] = array[row-j-1][i]
    }
  }
  return newArray
}

const isInBound = (ci, cj, N) => {
  return (0 <= ci && ci < N && 0 <= cj && cj < N)
}

const generalize = (coords) => {
  const is = [], js = []
  for (const coord of coords) {
    is.push(coord[0])
    js.push(coord[1])
  }
  const i_min = Math.min(...is), i_max = Math.max(...is)
  const j_min = Math.min(...js), j_max = Math.max(...js)
  coords.map((coord) => { 
    coord[0] -= i_min; 
    coord[1] -= j_min;
    return coord
  })

  // const n = Math.max(i_max-i_min, j_max-j_min) + 1
  const newShape = Array.from(Array(i_max-i_min+1), () => new Array(j_max-j_min+1).fill(0))
  for (const coord of coords) {
    const [i, j] = coord
    newShape[i][j] = 1
  }
  
  return newShape
}

const getShape = (i, j, visited, N, flag) => {

  const dfs = (i, j, visited, dx, coords, N) => {
    if (isInBound(i, j, N) && !visited[i][j]) {
      visited[i][j] = 1
      coords.push([i, j])

      for (const d of dx) {
        const ni = i + d[0]
        const nj = j + d[1]
        dfs(ni, nj, visited, dx, coords, N)
      }
    }
  }
  
  const dx = [[-1, 0], [1, 0], [0, -1], [0, 1]]
  const coords = []
  const generalShapes = new Set([])
  dfs(i, j, visited, dx, coords, N)

  let generalShape = generalize(coords)
  generalShapes.add(JSON.stringify(generalShape))
  
  if (flag) {
    return generalShapes
  }
  for (let i = 0; i < 3; i++) {
    generalShape = transpose(generalShape)
    generalShapes.add(JSON.stringify(generalShape))
  }
  
  return generalShapes
}

const isMatch = (shapeList, gameShapeList) => {
  const res = []
  for (const shape of shapeList) {
    for (let k = 0; k < gameShapeList.length; k++) {
      const isIn = gameShapeList[k].indexOf(...shape)
      if (isIn !== -1) {
        gameShapeList.splice(k, 1)
        res.push(shape)
        break
      }
    }
  }

  let total = 0
  for (const r of res) {
    const _r = JSON.parse(...r)
    
    for (const __r of _r) {
      total += __r.reduce((acc, curr) => acc + curr)
    }
  }
  return total
}

const solution = (game_board, table) => {
  let answer = 0
  const game_board_visited = [...game_board.map(arr => [...arr])]
  const table_visited = [...table.map(arr => [...arr].map(val => val > 0 ? 0 : 1))]
  const N = table.length
  const shapeList = []
  const gameShapeList = []

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      if (!table_visited[i][j]) {
        shapeList.push([...getShape(i, j, table_visited, N, true)])
      }
      if (!game_board_visited[i][j]) {
        gameShapeList.push([...getShape(i, j, game_board_visited, N, false)])
      }
    }
  }

  answer = isMatch(shapeList, gameShapeList)

  return answer
}

const game_board = [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,0,1,1,1,1],[0,0,0,0,1,0],[1,1,1,1,0,0]]
const table = [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,0,1,0,1,1],[0,1,1,0,0,0],[0,0,1,0,1,1],[0,1,0,0,0,0]]
console.log(solution(game_board, table))

// const a = [[0,0,0],[1,1,0],[1,1,1]]
// const b= [[1,1,1],[1,0,0],[0,0,0]]
// console.log(solution(a, b))